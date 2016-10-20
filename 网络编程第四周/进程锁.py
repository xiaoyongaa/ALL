from multiprocessing import Manager,Array
from multiprocessing import Process,queues
from multiprocessing import RLock,Lock,Event,Condition,Semaphore
import multiprocessing
import time


def foo(i,li,lock):
    lock.acquire()  #上锁
    li[0]=li[0]-1
    time.sleep(1)
    print("hi",li[0])
    lock.release()  #解锁




if __name__=="__main__":
    li=Array("i",1)
    li[0]=10
    lock=RLock()
    for i in range(10):
        p=Process(target=foo,args=(i,li,lock))
        p.start()

