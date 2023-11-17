from flask import Flask, request
from urllib.parse import unquote

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=["GET", "POST"])
def r():
    global result
    global result_form

    a = request.args
    form = request.form
    data = request.get_json()
    c = dict(request.headers)
    d = request.url
    e = request.remote_addr

    result_form = {"params": a, "body": form, "headers": c, "url": d, "ip": e}
    result = {"params": a, "body": data, "headers": c, "url": d, "ip": e}

    if request.form:
        return result_form
    else:
        return result

@app.route('/result1', methods=["GET"])
def d():
    content_type = result["headers"].get("Content-Type", "")

    if "json" in content_type:
        return result
    else:
        return result_form

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8899, debug=True)
