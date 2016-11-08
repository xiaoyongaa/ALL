import multiprocessing
from multiprocessing import Process,queues,Array,Manager
import time

#li=[]

def f(i,li):
    li[i]=i+100
    print(li.values())


if __name__=="__main__":
    #li=queues.Queue(20,ctx=multiprocessing)
    obj=Manager()
    li=obj.dict()
    for i in range(10):
        p=Process(target=f,args=(i,li))
        p.start()
        p.join()   #等待子进程
    #time.sleep(2)
