import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from databasemonitor import Sqldriver
from requests import request
from flask import Flask, request, jsonify,redirect,url_for
import uuid
import redis
import json



app = Flask(__name__)
pool = redis.ConnectionPool(host='60.204.173.77')
r = redis.Redis(connection_pool=pool)


@app.route('/oauth2/authorize',methods=['get'])
def a():
    params = request.args
    client_id = params.get("client_id")
    response_type = params.get("response_type")
    redirect_url  = params.get("redirect_url")
    code = "wsj123456"
    state = params.get("state")
    url = str(redirect_url) + "?state=" + str(state) + "&" + str(response_type) + "=" + str(uuid.uuid1()).replace("-","")
    if client_id == "123456":
        return  redirect(url)
@app.route('/oauth2/refreshtoken',methods=['get'])
def b():
     params = request.args
     grant_type = params.get("grant_type")
     code = params.get("code")
     client_id = params.get("client_id")
     client_secret = params.get("client_secret")
     refreshToken_value = str(uuid.uuid1())
     accessToken_value = str(uuid.uuid1())
     print(r.set("refreshToken", refreshToken_value, ex=120))
     print(r.set("accessToken",accessToken_value,ex =60 ))
     h = {"refreshToken":refreshToken_value,"accessToken":accessToken_value}
     h = json.dumps(h)
     if  client_secret =="654321" and  client_id  == "123456":
         return  h
     return "client_secret is error or client_id is error"
# @app.route('/oauth2/accessToken',methods=["get"])
# def c():
#     params = request.args
#     client_id = params.get("client_id")
#     client_secret = params.get("client_secret")
#     grant_type = params.get("grant_type")
#     redirect_uri = params.get("redirect_uri")
#     refresh_token = params.get("refresh_token")
#     accessToken_value = str(uuid.uuid1())
#     print(r.set("access_token", accessToken_value, ex=120))
#     print(r.get("access_token"))
#     k = {"access_token":accessToken_value}
#     if  client_id =="123456" and client_secret =="654321":
#         return k
#     return "client_secret is error or client_id is error"
@app.route('/oauth2/result',methods=["post"])
def d():
    params =request.args
    headers = request.headers
    data = request.data
    if  r.get("accessToken") is not  None:
        accessToken_value = str(r.get("accessToken"),encoding="utf-8")
        if   headers.get("accessToken") == accessToken_value:
            print(headers.get("accessToken"))
            return {"result": "距离accessToken过期还剩"+str(r.ttl("accessToken"))+"s"}
        if params.get("accessToken") ==accessToken_value:
            return {"result": "距离accessToken过期还剩"+str(r.ttl("accessToken"))+"s"}
        if   data  :
            data1 = json.loads(data)
            if data1.get("accesstoken")==accessToken_value:
              return  {"result": "距离accessToken过期还剩"+str(r.ttl("accessToken"))+"s"}
            else:
              return {"result":"请输入正确的body"}
        else:
            return{"result":"请输入正确的参数"}
    else:
         return {"result":"accesstoken已过期"}



executor = ThreadPoolExecutor()
app = Flask(__name__)
app.debug = True
# 把获取到的数据转为JSON格式。
result = {}



app.config['JSON_AS_ASCII'] = False
executor = ThreadPoolExecutor()


@app.route("/returnAll", methods=["get", 'post'])  # 发什么返回什么
def returnAll_run():
    if request.args:
        print(request.args)
        return request.args
    if request.form:
        return request.form
    else:
        return request.data


@app.route("/timeout", methods=['post'])
def timeout_run():
    time.sleep(600)
    return "接口执行完成，用时1分钟"


@app.route('/return', methods=["GET", "POST"])  # 返回body的固定格式
def return_run():
    global result
    global result_form

    a = request.args
    form = request.form
    data = request.get_json()
    c = dict(request.headers)
    d = request.url
    e = request.remote_addr

    result_form = {"params": a, "body": form, "headers": c, "url": d, "ip": e}
    result = {"params": a, "body": data, "headers": c, "url": d, "ip": e}

    if request.form:
        return result_form
    else:
        return result


slutionkey = ["70bb8ce5", "ea83deb4", "a2cb12af", "211190c1", "e2941c1c", "ce6efa87", "990a4eb0", "14b2d8e4"]
name = ["生产流程管理", "设备巡检", "工程项目管理", "零售进销存", "智能售后", "客户管理", "互联网产品研发", "招聘管理"]

"""
统计时长
"""
globalk = []
globalv = {'result': []}

def slutiontime():
    global globalk
    global globalv
    globalk = []
    globalv = {'result': []}
    print("yibukaishi")
    url_toekn = "https://qingflow.com/api/user/login"
    header_token = {"Content-Type": "application/json"}
    data_token = {
        "password": "JVFZIPB9tCrTBLMoGt/stfsjlu3YUT3ppQhnhSidIaviVdYXkOaO7IEs61N1N5KDG5Yf3XlXYjcF3jGeF8i8jPdox6rN8VUCA2f3eGKhrRH4UN0dCaJyGBDAlCxTJrMcyz38+w4nrd/IE0nW0IaZL9ZXTQkcVRuBFGToGgo6ZCI=",
        "mobile": "99992345677", "email": "", "areaCode": "86", "loginType": "sms"}
    r_token = requests.post(url=url_toekn, headers=header_token, json=data_token)
    b = json.loads(r_token.text)["token"]
    w = -1
    print(b)
    v = {'result': []}
    k = []
    for i in slutionkey:
        w = w + 1
        print(w)
        url = "https://qingflow.com/api/app"
        header = {"token": b, "wsId": "386678", "Content-Type": "application/json"}
        data = {"solutionKey": i, "beingCopyData": True, "solutionSource": "solutionDetail"}
        print(header)
        print(data)
        r = requests.post(url=url, json=data, headers=header)
        print(r.text)
        """
        删除安装的解决方案
        """
        dele = json.loads(r.text)["data"]["tagIds"]
        print(dele)
        url_delete = "https://api.qingflow.com/tag"
        data_delete = {"tagIds": dele, "clearAll": True}
        header_delete = {"accessToken": "042d5c66-5bf9-4290-951a-addec6f8e6e1", "Content-Type": "application/json"}
        r_delete = requests.delete(url=url_delete, headers=header_delete, json=data_delete)
        print(r_delete.text)
        h = r.elapsed.total_seconds()
        p = round(h, 1)
        print(p)
        x = str(p) + "s" + name[w] + "，"
        k.append(x)
        print(v)
    v["result"] = k
    print(k)
    globalk = k
    globalv = v
    return v


"""
启动安装解决方案
"""
@app.route('/jiankong', methods=['post'])
def jiankong_run():
    u = ""
    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    password = get_Data.get('password')
    if password == "wsj":
        executor.submit(lambda p: slutiontime(), u)
        return {"result": "开始安装解决方案～"}
    else:
        return {"result": '请输入正确的密钥'}


"""
查询解决方案耗时
"""
@app.route('/jiankong', methods=["get"])
def jiankong_result():
    params = request.args
    password = params.get("password")
    set1 = set(globalk)
    print(globalk)
    print(set1)
    if password == "wsj":
        if len(set1) >= 8:
            return globalv
        else:
            return {"reult": ["正在安装解决方案,请稍等～"]}
    else:
        return {"result": ["请输入正确的值"]}


"""
 启动线索监控
"""
response_signup1 = {"result": "这是第一次返回"}
@app.route('/mointor', methods=['post'])
def mointor_run():
    global response_signup1
    global counter_success
    global counter_fail
    counter = Sqldriver().find()
    print(counter)
    counter_success = counter[0][0]
    counter_fail = counter[0][3]
    c_toal = str(counter_success + counter_fail)
    print(c_toal)
    print("yibukaishi")
    url_singnup1 = "https://qingflow.com/api/share/user/signup"
    header_token = {"Content-Type": "application/json"}
    email = "767676" + c_toal + "@qq.com"
    mobile = "767676" + c_toal
    print(email)
    print(mobile)
    data_token = {"email": email,
                  "password": "Wsj123456",
                  "code": "767676", "mobile": mobile, "areaCode": "86", "source": "home_home",
                  "uuid": "544ae1f2-2553-4caa-ad70-745f5dab353b", "signUpSource": "home", "beingInvited": False,
                  "utmInfo": None, "bdVid": "", "beingPrivacyPolicy": True, "registerSource": "normal"}
    response_signup = requests.post(url=url_singnup1, headers=header_token, json=data_token)
    print(response_signup.json())
    response_signup1 = response_signup.json()
    k = json.dumps(response_signup1)
    if "token" in k:
        counter_success = counter_success + 1
        Sqldriver().update(counter_success=counter_success, counter_fail=counter_fail)
    else:
        counter_fail = counter_fail + 1
        Sqldriver().update(counter_success=counter_success, counter_fail=counter_fail)
    print(response_signup1)
    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    password = get_Data.get('password')
    if password == "wsj":
        return k
    else:
        return {"result": '请输入正确的参数'}


"""
查询线索结果
"""
@app.route('/mointor', methods=["get"])
def mointor_result():
    url_list = "https://api.qingflow.com/app/83da52bc/apply/filter"
    headers = {"Content-Type": "application/json", "accessToken": "ec60e8f0-db81-45db-aa7d-b1364408b623"}
    data_list = {"pageSize": 50, "pageNum": 1, "type": 8, "sorts": [], "queries": [], "queryKey": "767676"}
    response_list = requests.post(url=url_list, headers=headers, json=data_list).json()
    d = response_list["result"]["resultAmount"]
    print(d)
    params = request.args
    password = params.get("password")
    if password == "wsj":
        counter = Sqldriver().find()
        counter_success = counter[0][0]
        counter_fail = counter[0][3]
        return {"counter_success": str(counter_success), "counter_fail": str(counter_fail), "counter_qingliu": str(d)}


# 返回JSON数据。
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8801, debug=False)
    # app.run()
