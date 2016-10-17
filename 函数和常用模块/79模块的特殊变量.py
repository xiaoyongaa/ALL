#wewqe
import cash
import os
import sys
#print(vars(cash))
'''
print(__file__)  #脚本自己的名字
#print(__doc__)
path=os.path.abspath(__file__)  #获取绝对路径
print(path)
shangyiji=os.path.dirname(os.path.dirname(path)) #获取上一级目录
print(shangyiji)
sys.path.append(shangyiji)
'''
print(cash.__name__)
print(__name__)  #等于__main__ ，只有执行当前文件时候，
#__name__=__main__
'''
def u():
    print("wq")
if __name__ == '__main__':
    u()
'''