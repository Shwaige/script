import hashlib

from flask import Flask, request

app = Flask(__name__)

@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        token = '9612ab76ba4ec146e57c63c118b02d16'  # 替换为您在微信公众平台设置的 Token
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if hashlib.sha1(s.encode()).hexdigest() == signature:
            return echostr
        else:
            return 'Invalid Request'
    elif request.method == 'POST':
        # 处理微信服务器发送的消息与事件
        # 可以根据实际需求编写处理逻辑
        return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)