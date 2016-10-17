import time
def f1(arg):
    time.sleep(1)
    print(arg)

#创建多线程，得先导入一个模块
import threading
t=threading.Thread(target=f1,args=[1])  #创建了一个线程
t.setDaemon(True)  #设置不等此子线程，设置主线程是否等待子线程的执行
t.start() #不代表当前线程会被立即执行
t.join(1.0000001)  #表示主线程到此一直等待，直到子线程执行完毕,最多等2秒
                   #参数，表示主线程最多等待n秒
print("end")
print("end")
print("end")
print("end")
print("end")
print("end")
print("end")
print("end")
print("end")