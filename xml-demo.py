from flask import Flask, Response
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

app = Flask(__name__)

@app.route('/get_xml_data', methods=['GET'])
def get_xml_data():
    # 创建XML结构
    root = Element('root')

    # 创建第一个A元素
    a1 = SubElement(root, 'A')
    b1 = SubElement(a1, 'b')
    b1.text = '1'

    # 创建第二个A元素
    a2 = SubElement(root, 'A')
    b2 = SubElement(a2, 'b')
    b2.text = '2'

    # 将XML格式化为字符串
    xml_str = minidom.parseString(tostring(root)).toprettyxml(indent="  ", encoding="UTF-8")

    # 返回XML响应
    return Response(xml_str, content_type='text/xml')

if __name__ == '__main__':

    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=8805, debug=True)
