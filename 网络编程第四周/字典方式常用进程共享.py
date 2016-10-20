from multiprocessing import Manager
from multiprocessing import Process,queues
import multiprocessing
import time



def fun(i,li):
    li[i]=i+100
    print("hello",li)




if __name__=="__main__":
    obj=Manager()
    li=obj.dict()
    for i in range(10):
        p=Process(target=fun,args=(i,li))
        p.start()
        p.join()
        #time.sleep(0.1)



# 进程
# 基本使用
# 默认数据不共享
# queues  队列方式
# array  数组方式
# Manager.dict   字典方式


