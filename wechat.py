from datetime import time
from flask import Flask, request, make_response
import hashlib
import xml.etree.ElementTree as ET

app = Flask(__name__)
TOKEN = '9612ab76ba4ec146e57c63c118b02d16'  # 替换为您在微信公众平台设置的 Token

@app.route('/wechat', methods=['POST'])
def wechat():
    # 解析 XML 数据包
    xml_data = request.data
    xml_root = ET.fromstring(xml_data)

    # 提取出消息类型和文本内容
    msg_type = xml_root.find('MsgType').text
    content = xml_root.find('Content').text

    if msg_type == 'text':
        # 返回固定值
        reply_content = '您发送的消息是：' + content

        # 组装回复消息的 XML 格式
        reply_xml = f'''
            <xml>
                <ToUserName><![CDATA[{xml_root.find('FromUserName').text}]]></ToUserName>
                <FromUserName><![CDATA[{xml_root.find('ToUserName').text}]]></FromUserName>
                <CreateTime>{int(time.time())}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{reply_content}]]></Content>
            </xml>
        '''

        # 返回消息
        response = make_response(reply_xml)
        response.headers['Content-Type'] = 'application/xml'
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
