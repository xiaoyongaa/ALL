#!/usr/local/python3.5/bin/python3.5
import os
import time
import sys
import socket
path=os.getcwd()
os.chdir(path)
def check_port(ip,port):
    count=1
    for i in range(3):
        if count>=3:
            count=1
            #print(0)
            break
        else:
             s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             s.settimeout(1)
             try:
                s.connect((ip,port))
                #print(0)
                count=1
             except Exception:
                count+=1
                os.chdir(path)
                count=str(count)
                os.system("echo"+" "+count+" "+"&>cishu.txt")
                count=int(count)
             s.close()
    if os.path.exists("cishu.txt"):
        c=os.popen("cat cishu.txt").read().strip()
        c=str(c)
        if c=="3":
            os.system(">cishu.txt")
            print(1)

def run():
    ip=sys.argv[1]
    port=sys.argv[2]
    port=int(port)
    check_port(ip,port)

run()
