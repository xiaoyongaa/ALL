from multiprocessing import Array
from multiprocessing import Process,queues
import multiprocessing
li=Array("i",10)

def fun(i,li):
    li[i]=i+100
    for i in li:
        print(i)


if __name__=="__main__":
    for i in range(10):
        p=Process(target=fun,args=(i,li))
        p.start()