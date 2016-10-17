#!/usr/local/python3.5/bin/python3.5
import os
import time
import sys
import socket
path="/app/jboss-5.1.0.GA/server/"
export=os.system("export RUN_CONF=/app/jboss-5.1.0.GA/bin/run_longshine.conf")
user=os.popen("id | awk 'BEGIN{FS=\" \"}{print$1}' |awk 'BEGIN{FS=\"(\"}{print$2}'|sed  's/)//g'").read().strip()
if export==0:
    print("export is success!")
else:
    exit("export is ERROR")
class all:
    @staticmethod
    def start():
        stat=os.system("netstat -altunp | awk 'BEGIN{FS=\" \"}{print$4}' | awk 'BEGIN{FS=\":\"}{print$2}'| grep 1399 &>/dev/null")
        if stat==0:
            exit("longshine is starting")
        else:
            if user=="root":
                if os.path.exists(path+"longshine/tmp") and  os.path.exists(path+"longshine/work") and os.path.exists(path+"longshine/data"):
                    #print("cunzai")
                    r=os.system("rm -rf /app/jboss-5.1.0.GA/server/longshine/tmp   /app/jboss-5.1.0.GA/server/longshine/work  /app/jboss-5.1.0.GA/server/longshine/data")
                    re=os.system("su - jbossadm -c \"nohup /app/jboss-5.1.0.GA/bin/run.sh -c longshine --host=\"10.139.100.23\"> /dev/null &\"")
                    if re==0:
                        print("longshine is start success!")
                        return True
                    else:
                        exit("longshine is fail!!!")
                else:
                    exit("bu cunzai")
            elif user=="jbossadm":
                if os.path.exists(path+"longshine/tmp") and  os.path.exists(path+"longshine/work") and os.path.exists(path+"longshine/data"):
                    #print("cunzai")
                    re=os.system("nohup /app/jboss-5.1.0.GA/bin/run.sh -c longshine --host=\"10.139.100.23\"> /dev/null &")
                    r=os.system("rm -rf /app/jboss-5.1.0.GA/server/longshine/tmp   /app/jboss-5.1.0.GA/server/longshine/work  /app/jboss-5.1.0.GA/server/longshine/data")
                    if re==0:
                        print("longshine is start success!")
                        return True
                    else:
                        exit("longshine is fail!!!")
                else:
                    exit("bu cunzai")
            else:
                exit("please is in true user!!")
    @staticmethod
    def stop():
        stat=os.system("netstat -altunp | awk 'BEGIN{FS=\" \"}{print$4}' | awk 'BEGIN{FS=\":\"}{print$2}'| grep 1399 &>/dev/null")
        if stat==0:
            #print("longshine is starting")
            re=os.system("netstat -altunp |grep 1399 |awk 'BEGIN{FS=\" \"}{print$7}' | awk 'BEGIN{FS=\"/\"}{print$1}' &>/app/scripts/pid.txt")
            if re==0:
                #print("pid ok")
                pid=os.popen("cat /app/scripts/pid.txt").read().strip()
                kill=os.system("kill -9"+" "+pid)
                st=os.system("/app/jboss-5.1.0.GA/bin/shutdown.sh --server=\"10.139.100.23:1399\"")
                stat=os.system("netstat -altunp | awk 'BEGIN{FS=\" \"}{print$4}' | awk 'BEGIN{FS=\":\"}{print$2}'| grep 1399 &>/dev/null")
                if stat!=0:
                    print("longshine is stoping")
                    return True
                else:
                    exit("longshine is stoping ERROR")
            else:
                exit("pid is ERROR")
        else:
            exit("longshine is stoping")
    @classmethod
    def restart(cls):
        r=cls.stop()
        if r==True:
            print("stop is ok")
            r=cls.start()
            if r==True:
                print("start is ok")
        else:
            exit("stop is ERROR")
    @staticmethod
    def status():
        stat=os.system("netstat -altunp | awk 'BEGIN{FS=\" \"}{print$4}' | awk 'BEGIN{FS=\":\"}{print$2}'| grep 1399 &>/dev/null")
        if stat==0:
            #print("longshine is starting")
            re=os.system("netstat -altunp |grep 1399 |awk 'BEGIN{FS=\" \"}{print$7}' | awk 'BEGIN{FS=\"/\"}{print$1}' &>/app/scripts/pid.txt")
            pid=os.popen("cat /app/scripts/pid.txt").read().strip()
            if re==0:
                stat=os.popen("ps aux |grep -v grep |"+"grep"+" "+pid).read().strip()
                print(stat)
            else:
                exit("pid is ERROR")
        else:
            exit("longshine is stoping")
    @staticmethod
    def check_port():
        ip="127.0.0.1"
        port=int(9309)
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
          s.connect((ip,port))
          print("OSGI port:9309 is ok!!!")
        except Exception:
          print("OSGI port:9309 is down!!!")
        s.close()
    @classmethod
    def run(cls):
        if sys.argv[1]=="start":
            cls.start()
            time.sleep(30)
            cls.check_port()
        elif sys.argv[1]=="stop":
            cls.stop()
            time.sleep(4)
            cls.check_port()
        elif sys.argv[1]=="restart":
            cls.restart()
            time.sleep(30)
            cls.check_port()
        elif sys.argv[1]=="status":
           cls.status()
           time.sleep(4)
           cls.check_port()
        else:
           print("please input ERROR")


obj=all()
obj.run()
