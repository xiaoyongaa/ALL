import re
import pickle
import os
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
path=path+"\db"
os.chdir(path)


def chulikuohao():
    while True:
        shu=pickle.load(open("shu.txt","rb"))
        if "(" in shu or ")" in shu:
            print(eval(shu))
            e=re.search(r"\(([\+\-\*\/]*\d){0,}\)",shu)
            e=e.group()
            key=e
            r=e.replace("(","")
            r=r.replace(")","")
            r=eval(r)
            r=str(r)
            sh=shu.replace(key,r)
            pickle.dump(sh,open("shu.txt","wb"))
            break

def sum():
    shu=pickle.load(open("shu.txt","rb"))
    r=re.findall("\d{0,}[\+\-\*\/]{0,}",shu)
    with open("re.txt","w") as tt:
        for i in r:
            tt.write(i)
    with open("re.txt","r") as yy:
        yy=yy.read()
    print(eval(yy))

def run():
    shu=input("请输入你要计算的表达式:")
    shu=shu.strip()
    pickle.dump(shu,open("shu.txt","wb"))
    #shu="8*12+(10000-(5*6*7)+(1+1)/77+2)*(10-7)+(10-7)+8+(9+1)"
    if "(" in shu or ")" in shu:
        #print("存在括号，优先处理")
        chulikuohao()
    else:
        #print("不存在括号，直接计算")
        sum()

if __name__=="__main__":
    run()