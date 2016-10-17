#八、XML
#XML是实现不同语言或程序之间进行数据交换的协议
#处理XML文本的模块
from xml.etree import ElementTree
import requests
import urllib
tree=ElementTree.parse("1.xml")   #加载到对象里面
root=tree.getroot()  #获取根节点
#print(root)
#print(root.tag)#获取根节点名
#print(root.attrib) #获取根节点属性
#print(root.iter("yes"))
for node in root.iter('year'):
    # 节点的标签名称和内容
    #print(node.tag, node.text)
    # 将year节点中的内容自增一
    new=int(node.text)+1
    new=str(new)
    node.text=new

     # 设置属性
    node.set("name","dsad")
    node.set("age","18")


    #删除属性
    del node.attrib["age"]
    print(node.tag, node.text,node.attrib)

############ 保存文件 ############
tree = ElementTree.ElementTree(root)
tree.write("newnew.xml", encoding='utf-8')
############ 保存文件 ############
'''
for child in root:
    print(child.tag,child.attrib)
    for shunzi in child:
        print(shunzi.tag,shunzi.text) #获取节点名，内容
        '''

'''
from xml.etree import ElementTree as ET

# 直接解析xml文件
tree = ET.parse("xo.xml")

# 获取xml文件的根节点
root = tree.getroot()
'''