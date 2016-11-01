import os
path="E:\git"  #定义要检查容量的目录
def all(path):
    size=0
    for root,dirs,files in os.walk(path):
        for item in files:
            size=size+os.stat(os.path.join(root,item)).st_size
    return size
size=all(path)
print(size)