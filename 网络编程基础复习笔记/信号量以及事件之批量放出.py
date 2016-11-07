import threading
import time
num=10
def run(i,loock):
    global num
    loock.acquire()
    num=num-1
    time.sleep(2)
    print(num,i)
    loock.release()

loock=threading.BoundedSemaphore(5)
for i in range(30):
    t=threading.Thread(target=run,args=(i,loock))
    t.start()