import time
import threading
def f1(i):
    time.sleep(3)
    print(i)



# f1(1)
# f1(2)

xiancheng1=threading.Thread(target=f1,args=(1,))
xiancheng2=threading.Thread(target=f1,args=(2,))
xiancheng1.start()
xiancheng2.start()

#
# for i in range(10):
#     xiancheng=threading.Thread(target=f1,args=(i,))
#     xiancheng.start()


'''
python多线程有全局解释器锁，GIL。同一个进程只有1个线程才能出来
IO操作,不占用CPU.用多线程，提高并发,线程并行
计算型操作，占用CPU,用多进程，提高并发,进程并行

'''