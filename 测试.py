from flask import Flask, request
import json
app = Flask(__name__)
app.debug = True
@app.route("/", methods=['post'])
def check():
    # 默认返回内容
    a0 = json.loads(request.data)
    a = a0["a"]
    b = a.split("@")
    b1 = str(b[0])
    return  b1
if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0",port=8803,debug=True)
# a0 = {"a":"11@22"}
# a = a0["a"]
# b = a.split("@")
# b1 = str(b[0])
#
# print(b1)