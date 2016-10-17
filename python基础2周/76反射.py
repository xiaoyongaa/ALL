#利用字符串的形式去对象中（模块中）(寻找/检查/删除/设置）成员
long=getattr(commad,"login")
            #从commad模块中找到login函数
hasattr(comms,"lomgiun")
#setattr()模块里面设置个成员，基于内存的
#delattr()模块里面删除成员，基于内存的
choose=input("请输入你要访问的页面: ")
    m,f=choose.split("/")
    print(m,f)
    m=__import__("commad")
#模块也可以通过字符串形势导入
'''
反射
实例：伪造的web框架的路由系统
反射：基于字符串的形势去对象（模块）中操作其成员
getattr(),setattr(),delattr(),hasattr()
获取对象中成员，设置对象中成员，删除对象中成员，判断对象中成员
扩展：导入模块
import xxx
from xxxx import xxxx
obj=__import__("xxxx")
obj=__import__("xxxx",fromlist=True)
'''

#