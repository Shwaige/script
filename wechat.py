from flask import Flask, request
import hashlib

app = Flask(__name__)


@app.route('/wechat', methods=['GET'])
def wechat():
    # 处理微信服务器发送的消息与事件
    # 这里假设您已经根据实际需求编写了处理逻辑，并将回复消息存储在 reply_text 中
    reply_text = "Hello, this is your Flask API!"

    # 返回文本消息给微信服务器
    return reply_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

