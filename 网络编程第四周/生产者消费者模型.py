import queue
import threading
import time
q=queue.Queue()  #

#买票的
def productor(i):
        q.put(i,"包子")


#处理买票
def connsumer(i):
    while True:
        print(i,q.get())
        time.sleep(2)
        #q.get()


#创建300个用户，一起买票
for i in range(300):
    t=threading.Thread(target=productor,args=(i,))
    t.start()


#处理票 3台机器
for j in range(3):
    t=threading.Thread(target=connsumer,args=(j,))
    t.start()



