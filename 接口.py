import requests
from flask import Flask, request, jsonify
import json
app = Flask(__name__)
app.debug = True
# 把区获取到的数据转为JSON格式。
result = {}
@app.route("/",methods=["GET",'post'])
def add_stu():
    if request.args :
        print(request.args)
        return request.args
    if request.form:
         return request.form        
    else:
        return request.data
# @app.route("/return", methods=["post"])
# def test():
#     if request.args:
#         return request.args
#     else:
#         return request.data
# @app.route("/return", methods=["post","get"])
# def test2():
#     if not request.headers:
#         return ("fail")
#     else:
#         return request.headers

 # 返回JSON数据。
if __name__ == '__main__':
  app.run(host="0.0.0.0",port=8890,debug=True)
   # app.run()



