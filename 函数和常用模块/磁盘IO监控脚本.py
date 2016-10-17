#!/usr/local/python3.5/bin/python3.5
import os
import sys
import time
def run():
    r=os.system("/usr/bin/iostat  -d -p -k |grep xvdb1 &>/dev/null")
    if r==0:
       if sys.argv[1]=="read":
            read()
            return True
       elif sys.argv[1]=="write":
           write()
       else:
           print("please input ERROR")
    else:
       return False

def read():
    kB_read=os.popen(" /usr/bin/iostat  -d -p -k |grep xvdb1 |awk 'BEGIN{FS=\" \"}{print$5}'").read()
    old=int(kB_read.strip())
    time.sleep(10)
    kB_read=os.popen(" /usr/bin/iostat  -d -p -k |grep xvdb1 |awk 'BEGIN{FS=\" \"}{print$5}'").read()
    new=int(kB_read.strip())
    new=new-old
    print(new)

def write():
    kB_wrtn=os.popen(" /usr/bin/iostat  -d -p -k |grep xvdb1 |awk 'BEGIN{FS=\" \"}{print$6}'").read()
    old=int(kB_wrtn.strip())
    time.sleep(10)
    kB_wrtn=os.popen(" /usr/bin/iostat  -d -p -k |grep xvdb1 |awk 'BEGIN{FS=\" \"}{print$6}'").read()
    new=int(kB_wrtn.strip())
    new=new-old
    print(new)


run()