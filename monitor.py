import json
import requests
from flask import  Flask,request
from concurrent.futures import ThreadPoolExecutor
from databasemonitor import  Sqldriver
executor = ThreadPoolExecutor()
app = Flask(__name__)
response_signup1 ={"result":"这是第一次返回"}

@app.route('/mointor',methods=['post'])
def  run():
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
       return {"result":'请输入正确的参数'}
"""
查询结果
"""
@app.route('/',methods=["get"])
def  result():
   url_list = "https://api.qingflow.com/app/83da52bc/apply/filter"
   headers = {"Content-Type":"application/json","accessToken":"ec60e8f0-db81-45db-aa7d-b1364408b623"}
   data_list = {"pageSize":50,"pageNum":1,"type":8,"sorts":[],"queries":[],"queryKey":"767676"}
   response_list =requests.post(url=url_list,headers=headers,json=data_list).json()
   d = response_list["result"]["resultAmount"]
   print(d)
   params = request.args
   password = params.get("password")
   if password == "wsj":
       counter = Sqldriver().find()
       counter_success = counter[0][0]
       counter_fail = counter[0][3]
       return {"counter_success":str(counter_success),"counter_fail":str(counter_fail),"counter_qingliu":str(d)}
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8809)
# #
