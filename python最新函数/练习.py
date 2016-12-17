#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import os,sys,re
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
file_path="G:\\test\\NFNN6.0103_20161212124243.CP1"
file_path_shang=os.path.dirname(file_path)+"\\NFNN6.0103_20161212124243.CP1.bak"
print(file_path_shang)




def start():
    with open(file_path,"r") as old,open(file_path_shang,"w") as new:
        c=1
        f=True
        for i in old:
            c=c+1
            if c==45 and f==True:
                f=False
                continue
            elif c==123 and f==False:
                f=True
                continue
            elif f==False:
                new.write(i)








start()








