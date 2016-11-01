import os
path="E:\git"  #定义要检查容量的目录
def all(path):
    size=0
    for i in os.walk(path):
        for y in i[-1]:
            print(os.path.join(i[0],y))

all(path)
