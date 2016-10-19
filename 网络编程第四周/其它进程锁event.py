import threading
lock=threading.Event()

def func(i,lock):
    print(i)
    lock.wait()   #检测是什么灯，如果是红灯，就停
    print(i+100)



for i in range(10):
    t=threading.Thread(target=func,args=(i,lock))
    t.start()

#############################################
lock.clear()  #设置成红灯
inp=input(">>>:").strip()
if inp=="1":
    lock.set()  #设置成绿灯