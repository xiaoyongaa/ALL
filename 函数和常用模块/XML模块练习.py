#'son', {'name': '儿1'}
from  xml.etree import ElementTree
from xml.dom import minidom
def prettify(elem):
    """将节点转换成字符串，并添加缩进。
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

root=ElementTree.Element("root")  #


son1=ElementTree.Element("son1",{"name":"儿1"})
son2=ElementTree.Element("son2",{"name":"儿2"})


shuzhi1=ElementTree.Element("shunzhi1",{"name":"shuzhi1"})
shuzhi2=ElementTree.Element("shunzhi2",{"name":"shuzhi2"})
son1.append(shuzhi1)
son2.append(shuzhi2)


root.append(son1)
root.append(son2)

#tree=ElementTree.ElementTree(root)  #转换成tree类
#print(type(tree))
#tree.write("xxxoo.xml",encoding="utf-8")
#print(type(root))
s=prettify(root)
print(s)
with open("xxxoo.xml","w") as n:
    n.write(s)


