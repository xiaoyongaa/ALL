import os
print(os.sep)
path=os.path.abspath(__file__)
path=os.path.dirname(path)
print(path)
path=os.path.join(path,"t\\")  ##路径的拼接
print(path)
