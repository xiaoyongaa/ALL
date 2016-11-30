import os
import sys
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
from src import init_mysql   #导入模块
obj=init_mysql.init_mysql()  #创建对象
if hasattr(obj,"main"):
    fun=getattr(obj,"main")
    fun()
