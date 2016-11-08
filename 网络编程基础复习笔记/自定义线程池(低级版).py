import queue
import threading
import time
class ThreaPool:
    def __init__(self,maxsize):    #创建类时候构造方法
        self.maxsize=maxsize
        self.q=queue.Queue(maxsize)
        for i in range(maxsize):
            self.q.put(threading.Thread)    #循环放入线程类

    def get_thread(self):   #获取队列线程值
        return self.q.get()

    def add_thread(self):   #增加线程值  (消耗完最大线程值之后，要往里面增加线程)
        self.q.put(threading.Thread)


def task(i,pool):
    print(i,pool)
    time.sleep(1)
    pool.add_thread()


pool=ThreaPool(5)    #创建自定义线程对象，最大线程数为5

for i in range(100):
    t=pool.get_thread()  #获取队列线程值 是队列里面的类
    xiancheng=t(target=task,args=(i,pool,))    #线程对象
    xiancheng.start()




