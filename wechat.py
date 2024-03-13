from flask import Flask, request
import hashlib

app = Flask(__name__)
TOKEN = 'your_token'  # 替换为您在微信公众平台设置的 Token

def check_signature():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')

    tmp_arr = [TOKEN, timestamp, nonce]
    tmp_arr.sort()
    tmp_str = ''.join(tmp_arr)
    tmp_str = hashlib.sha1(tmp_str.encode()).hexdigest()

    if tmp_str == signature:
        return True
    else:
        return False

@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        if check_signature():
            return request.args.get('echostr', '')
        else:
            return 'Invalid Request'
    elif request.method == 'POST':
        # 处理微信服务器发送的消息与事件
        return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
