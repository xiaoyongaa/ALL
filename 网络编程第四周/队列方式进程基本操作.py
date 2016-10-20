from multiprocessing import Process,queues
import multiprocessing
li=queues.Queue(20,ctx=multiprocessing)

def fun(i,li):
    li.put(i)
    print("hello",i,li.qsize())


if __name__=="__main__":
    for i in range(10):
        p=Process(target=fun,args=(i,li))
        p.start()

