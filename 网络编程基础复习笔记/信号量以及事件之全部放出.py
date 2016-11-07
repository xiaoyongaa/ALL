import threading
event=threading.Event()
def func(i,event):
    print(i)
    event.wait()  #检测是什么灯
    print(i+100)

for i in range(10):
    t=threading.Thread(target=func,args=(i,event,))
    t.start()

###################
event.clear()   #设置成红灯
inp=input(">>>>")
if inp=="1":
    event.set() #设置成绿灯


