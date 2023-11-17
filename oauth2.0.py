from requests import request
from flask import Flask, request, jsonify,redirect,url_for
import uuid
import redis
import json
app = Flask(__name__)
pool = redis.ConnectionPool(host='110.42.144.188',password='wsj123456')
r =redis.Redis(connection_pool=pool)


@app.route('/oauth2/authorize',methods=['get'])
def a():
    params = request.args
    client_id = params.get("client_id")
    response_type = params.get("response_type")
    redirect_url  = params.get("redirect_url")
    code = "wsj123456"
    state = params.get("state")
    url =   url = str(redirect_url) + "?state=" + str(state) + "&" + str(response_type) + "=" + str(uuid.uuid1()).replace("-","")
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



if __name__ == "__main__":
    app.run(debug=False,port=8810,host="0.0.0.0")
