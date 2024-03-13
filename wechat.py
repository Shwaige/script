from flask import Flask

app = Flask(__name__)

@app.route('/wechat')
def wechat():
    return 'Hello, this is your Flask API!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)