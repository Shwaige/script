import os
import base64
import threading
from copy import deepcopy
from queue import Queue

from requests import post, get
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA


class ThreadCommon(threading.Thread):
    def __init__(self, task_queue: Queue = None, target=None, kwargs=None):
        super().__init__()
        self._task_queue = task_queue
        self._target = target
        if kwargs is None:
            self._kwargs = {}
        else:
            self._kwargs = kwargs

    def run(self) -> None:
        print('启动线程{}'.format(self.name))
        try:
            data = self._task_queue.get(False)
            self._target(data, **self._kwargs)
        except Exception as e:
            pass


def base_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def _encrpt(string, public_key):
    rsakey = RSA.importKey(public_key)  # 读取公钥
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    # 因为encryptor.encrypt方法其内部就实现了加密再次Base64加密的过程，所以这里实际是通过下面的1和2完成了JSEncrypt的加密方法
    encrypt_text = cipher.encrypt(string.encode())  # 1.对账号密码组成的字符串加密
    cipher_text_tmp = base64.b64encode(encrypt_text)  # 2.对加密后的字符串base64加密
    return cipher_text_tmp.decode()


def gen_body(pwd, public_key=None):
    '''根据账号密码生成请求的body然后调用_encrpt方法加密'''

    if not public_key: public_key = ''  # 输入对应的公钥
    key = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
    encrypt_res = _encrpt(pwd, key)
    return encrypt_res


def get_pubkey(base_url):
    url = os.path.join(base_url, 'api/user/pubkey')
    headers = deepcopy(base_headers())
    res = get(url, headers=headers)
    resp = res.json()
    if resp['code'] != 0:
        assert 0, 'api/user/pubkey请求错误：{}'.format(resp)
    return resp['data']['pubkey']


def post_data(user_id, email):
    return {
        "userId": user_id,
        "name": email,
        "areaCode": "",
        "mobileNum": "",
        "email": email,
        "headImg": "",
        "department": [],
        "role": [],
        "customRole": [],
        "customDepartment": [],
        "beingDisabled": "false"
    }


def get_post_queue(num, prefix):
    task_queue = Queue(0)
    for i in range(num):
        user_id = prefix + str(i)
        email = user_id + '@qq.com'
        data = post_data(user_id, email)
        task_queue.put(data)
    return task_queue


def user_create_and_pwd(json, old_pwd, new_pwd, base_url, access_token):
    try:
        url = os.path.join(base_url, 'openApi/user')
        headers = {**deepcopy(base_headers()), 'accessToken': access_token, 'content-type': 'application/json'}
        res = post(url, json=json, headers=headers)
        resp = res.json()
        if resp['errCode'] != 0:
            assert 0, '创建成员失败，错误详情：{}'.format(resp)

        # 初始化密码
        url = os.path.join(base_url, 'api/user/pwd')
        data = {
            "password": old_pwd, "mobile": "", "email": json['email'], "areaCode": "86", "loginType": "email"
        }
        headers = {**deepcopy(base_headers()), 'content-type': 'application/json'}
        res = post(url, json=data, headers=headers)
        resp = res.json()
        if resp['code'] != 0:
            assert 0, 'api/user/pwd请求错误：{}'.format(resp)
        ws_id = resp['data'][0]['wsId']

        url = os.path.join(base_url, 'api/user/login/uid')
        data = resp['data'][0]
        data['loginType'] = "EMAIL"
        res = post(url, json=data, headers=headers)
        resp = res.json()
        if resp['code'] != 0:
            assert 0, 'api/user/login/uid请求错误：{}'.format(resp)

        login_token = resp['data']['loginToken']
        url = os.path.join(base_url, 'api/user/pwd/init')
        headers = {**deepcopy(base_headers()), 'content-type': 'application/json', 'logintoken': login_token,
                   'wsid': str(ws_id)}
        data = {
            "oldPassword": old_pwd, "password": new_pwd, "verifyPassword": new_pwd
        }
        res = post(url, json=data, headers=headers)
        resp = res.json()
        if resp['code'] != 0:
            assert 0, 'api/user/pwd/init请求错误：{}'.format(resp)
        print('创建账号并重置密码成功！')
    except Exception as e:
        print(e)


def run(thread_num, usr_num=2000, usr_prefix='Qtest', base_url='https://www.scholarshipsgateway.gov.sg',
        access_token='e3f4decf-41af-42b3-863e-905780d8cf5f', new_pwd='Qflow_955'):
    """执行函数

    :param thread_num: 线程数，推荐10-20
    :param usr_num: 要创建的账号数
    :param usr_prefix: 测试数据前缀标识
    :param base_url: 接口域名
    :param access_token:
    :param new_pwd: 账号新密码
    :return:
    """
    task_queue = get_post_queue(num=usr_num, prefix=usr_prefix)
    pubkey = get_pubkey(base_url)
    old_pwd = gen_body('123456', pubkey)
    new_pwd = gen_body(new_pwd, pubkey)

    # data = post_data('test01', 'test01@qq.com')
    #
    # user_create_and_pwd(data, old_pwd, new_pwd, base_url, access_token)

    while not task_queue.empty():
        thread_list = []
        for i in range(thread_num):
            sub_thread = ThreadCommon(task_queue, user_create_and_pwd,
                                      kwargs={'old_pwd': old_pwd, 'new_pwd': new_pwd, 'base_url': base_url,
                                              'access_token': access_token})
            sub_thread.start()
            thread_list.append(sub_thread)

        for sub_thread in thread_list:
            sub_thread.join()


if __name__ == '__main__':
    # 执行前先安装pycryptodome、requests模块
    # pip install pycryptodome
    # pip install requests
    run(10, 2000)
