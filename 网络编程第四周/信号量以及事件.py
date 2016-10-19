import threading
import time
#lock=threading.Lock()  #创建锁对象,只能锁一次
#lock=threading.RLock()  #多层锁，一般用这个
lock=threading.BoundedSemaphore(5)  #信号量方式加锁

num=10


def func(i,lock):
    global num
    #上锁
    lock.acquire()   #上锁,30,5
    num-=1
    #lock.acquire()    #上锁
    time.sleep(2)
    #lock.release()     #开锁
    print(num,i)
    #开锁
    lock.release()    #开锁


for i in range(30):
    t=threading.Thread(target=func,args=(i,lock,))
    t.start()


#同一时刻只允许一个线程来操作
