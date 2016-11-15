import threading
import time
num=10
def run(i,event):
    print(i)
    event.wait()  #判断是什么状态
    print(i+100)


#lock=threading.RLock()
event=threading.Event()

for i in range(10):
    t=threading.Thread(target=run,args=(i,event))
    t.start()

event.clear()  #设置成红灯
inp=input(">>>")
if inp=="1":
    event.set()