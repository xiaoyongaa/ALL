import queue
import threading
import time

q=queue.Queue()



def productor(arg):
    q.put(str(arg))



def consumer(arg):
    while True:
        print(arg,q.get())
        time.sleep(2)






for i in range(300):
    t=threading.Thread(target=productor,args=(i,))
    t.start()



for j in range(3):
    t=threading.Thread(target=consumer,args=(j,))
    t.start()



