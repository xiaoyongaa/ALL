import threading
import time
def f1(arg):
    time.sleep(1)
    print(arg)


xiancheng=threading.Thread(target=f1,args=(123,))
#xiancheng.setDaemon(False)    #表示主线程不等此子线程
xiancheng.start()  #不代表当前线程会被立即执行
xiancheng.join(1.1)   #表示主线程到此，等待..直到子线程执行结束
print("end-----")     #参数，表示主线程在此最多等待N秒



