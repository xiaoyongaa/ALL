import multiprocessing
from multiprocessing import Process,queues,Array,Manager,RLock
import time

#li=[]

def f(i,li,lock):
    #lock.acquire()
    li=li-1
    #time.sleep(1)
    print(li)
    #lock.release()

if __name__=="__main__":
    lock=RLock()
    #li=Array("i",1)

    li=10
    #li[0]=10
    print(li)
    for i in range(10):
        p=Process(target=f,args=(i,li,lock))
        p.start()
        p.join()   #等待子进程
    #time.sleep(2)
