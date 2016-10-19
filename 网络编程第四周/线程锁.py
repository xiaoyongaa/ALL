import threading
import time
#lock=threading.Lock()  #创建锁对象,只能锁一次
lock=threading.RLock()  #多层锁，一般用这个
num=10


def func(lock):
    global num
    #上锁
    lock.acquire()   #上锁
    num-=1
    lock.acquire()    #上锁
    time.sleep(1)
    lock.release()     #开锁
    print(num)
    #开锁
    lock.release()    #开锁


for i in range(10):
    t=threading.Thread(target=func,args=(lock,))
    t.start()


#同一时刻只允许一个线程来操作