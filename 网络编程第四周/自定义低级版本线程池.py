#一个容器指定最大个数
#取一个少一个
#无线程时等待
#线程执行完毕，交还线程
import threading
import queue
import time
class thead_pool():
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.q=queue.Queue(maxsize)
        for i in range(maxsize):
            self.q.put(threading.Thread)   #放入线程类

    def get_thread(self):
        return self.q.get()


    def put_thread(self):
        self.q.put(threading.Thread)

pool=thead_pool(5)   #pool对象

def task(i,pool):
    print(i)
    time.sleep(1)
    pool.put_thread()



for i in range(100):
    t=pool.get_thread()   #取出t类,最多取5个就取不到了
    obj=t(target=task,args=(i,pool))  #创建线程,最多创建5个
    obj.start()


