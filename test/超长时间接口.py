from flask import Flask, request
import json
import time
app = Flask(__name__)
app.debug = True
@app.route("/", methods=['post'])

def long_delay():
    # 模拟一个需要1分钟的计算任务
    time.sleep(60)
    return "接口执行完成，用时1分钟"

if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0",port=8803,debug=True)