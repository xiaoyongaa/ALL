from xml.etree import ElementTree
str_xml=open("1.xml","r").read()
root=ElementTree.XML(str_xml)


ele=ElementTree.Element("xiaoyong",{"1":"2"})
root.append(ele)
print(root.attrib)
for i in root:
    print(i.tag,i.attrib,i.text)

##保存文件
tree=ElementTree.ElementTree(root)
tree.write("11.xml",encoding="utf-8")