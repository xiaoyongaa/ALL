from xml.etree import ElementTree as ET
# 打开文件，读取XML内容
str_xml = open('xo.xml', 'r').read()
# 将字符串解析成xml特殊对象，root代指xml文件的根节点
root = ET.XML(str_xml)