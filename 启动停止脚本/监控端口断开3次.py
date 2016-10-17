#!/usr/local/python3.5/bin/python3.5
import os
import time
path=os.getcwd()
os.chdir(path)
def check_port(self,port1):
    count=1
    for i in range(3):
        if count>=3:
            count=1
            #print(0)
            break
        else:
             re=os.system("netstat -altunp | awk 'BEGIN{FS=\" \"}{print$4}' | awk 'BEGIN{FS=\":\"}{print$2}'| grep "+"^"+port1+" "+">&/dev/null")
             if re==0:
                count=1
             else:
                count+=1
                os.chdir(path)
                with open("cishu.txt","w") as c:
                    count=str(count)
                    c.write(count)
                count=int(count)
    if os.path.exists("cishu.txt"):
        with open("cishu.txt","r") as n:
            c=n.read()
            if c=="3":
                os.system(">cishu.txt")
                print(0)
class check:
    def run(self):
        if sys.argv[1].isdigit():
            port1=sys.argv[1]
            check_port(self,port1)
        else:
            exit("please input port ERROR")

obj=check()
obj.run()