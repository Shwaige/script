from flask import Flask, Response
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

app = Flask(__name__)

@app.route('/get_xml_data', methods=['GET'])
def get_xml_data():
    # 创建XML结构
    root = Element('people')
    root.set('xmlns:xul', 'http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul')

    person1 = SubElement(root, 'person')
    name1 = SubElement(person1, 'name', first='george', last='bush')
    address1 = SubElement(person1, 'address', street='1600 pennsylvania avenue', city='washington', country='usa')
    phoneNumber1 = SubElement(person1, 'phoneNumber')
    phoneNumber1.text = '202-456-1111'

    person2 = SubElement(root, '{http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul}person')
    name2 = SubElement(person2, '{http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul}name', first='tony', last='blair')
    address2 = SubElement(person2, '{http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul}address', street='10 downing street', city='london', country='uk')
    phoneNumber2 = SubElement(person2, '{http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul}phoneNumber')
    phoneNumber2.text = '020 7925 0918'

    # 将XML格式化为字符串
    xml_str = minidom.parseString(tostring(root)).toprettyxml(indent="  ")

    # 返回XML响应
    return Response(xml_str, content_type='text/xml')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8899, debug=True)
