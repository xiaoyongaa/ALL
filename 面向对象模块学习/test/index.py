import os
import sys
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
os.chdir(path)
sys.path.append(path)
from config import *   #把类的名字导入进来和模块路径导入进来
#from back import code  #导入框架源码
mode1=__import__(pat,fromlist=True)  #把模块字符串化
if hasattr(mode1,classname):
    cls=getattr(mode1,classname)
    obj=cls()
    obj.f1()



