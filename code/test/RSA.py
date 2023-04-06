import json
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA

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

# 定义加密所需的参数
pwd = 'password123'
public_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCo/FEQ9gWvoUasO+POmAmjOFsBgACvzVRr8pRz1SrHmyP1TFNnrw89iPsgEAihRDaNJzm/Gu+z3mzZ6hS389yC3dU1Km6/mtIS+9+xQNpQVg0AeIfSEs80h5TVnOg/ip1BAyqxMTRE7Ta7lA2bcVjbYwj5fmckDAwIhi30yokkTwIDAQAB"'

# 调用gen_body函数生成加密后的字符串
encrypted_str = gen_body(pwd, public_key)

# 打印加密后的字符串
print(encrypted_str)