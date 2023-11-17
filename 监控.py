import json
from concurrent.futures import ThreadPoolExecutor

import requests
from flask import Flask, request

executor = ThreadPoolExecutor()
app = Flask(__name__)
v = {'result': []}
k = []
taskid = ""
"""
04a533ed  复工防疫
ea83deb4 设备巡检2.0
cbd896fb 工程项目管理
1ef2c3f5    互联网产品研发
e2941c1c  智能售后
bd73db01  集成式智能生产
597de24a   客户管理
14b2d8e4   招聘管理
"""
slutionkey = ["04a533ed", "ea83deb4", "1ef2c3f5", "e2941c1c", "bd73db01", "597de24a", "14b2d8e4"]
name = ["复工防疫", "设备巡检2.0", "互联网产品研发", "智能售后", "集成式智能生产", "客户管理", "招聘管理"]
"""

统计时长

"""


def slutiontime():
    print("yibukaishi")
    url_toekn = "https://uat.oalite.com/api/user/login"
    header_token = {"Content-Type": "application/json"}
    data_token = {
        "password": "fnIe4Sb/Mj+7pnWaJMnl6Gqxx4ofRqzjAVifCGBPDEBzN33yO/qqJEj3W4Ntp2ALAeYaa6j1m4zaH2m0URE00h6ItXmOKmn2tweLi+1N+s5nApFK1BtAnjyVWs20FmdIUO9EDu9v8JvXd4mQQSA2mCU+54gxf/ZDMjDYaXhV5JM=",
        "mobile": "999925298", "email": "", "areaCode": "86", "loginType": "sms"}
    r_token = requests.post(url=url_toekn, headers=header_token, json=data_token)
    b = json.loads(r_token.text)["token"]
    w = -1
    for i in slutionkey:
        w = w + 1
        print(w)
        url = "https://uat.oalite.com/api/app"
        header = {"token": b, "wsId": "110196", "Content-Type": "application/json"}
        data = {"solutionKey": i, "beingCopyData": True, "solutionSource": "solutionDetail"}
        print(header)
        print(data)
        r = requests.post(url=url, json=data, headers=header)
        h = r.elapsed.total_seconds()
        p = round(h, 1)
        print(p)
        x = str(p) + "s" + name[w] + "，"
        k.append(x)
        print(k)
        v["result"] = k
        print(v)
    return v


"""
启动安装解决方案
"""


@app.route('/jiankong', methods=['post'])
def run():
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


@app.route('/', methods=["get"])
def result():
    params = request.args
    password = params.get("password")
    set1 = set(k)
    if password == "wsj":
        if len(set1) == 7:
            return v
        else:
            return {"reult": ["正在安装解决方案,请稍等～"]}
    else:
        return {"result": ["请输入正确的值"]}


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8804)
