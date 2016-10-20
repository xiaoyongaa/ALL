'''
#线程
基本使用
线程锁
自定义线程池
############################
#进程
基本使用
进程锁
进程的数据共享
    默认数据不共享
    queues
    array
    Manager.dict
进程池 系统默认有 不需要自己写
'''
import time
from  multiprocessing import Pool #导入了进程池
def f1(a):
    time.sleep(1)
    print(a)

if __name__=="__main__":
    pool=Pool(5)  #创建进程池对象
    for i in range(30):
        #pool.apply(func=f1,args=(i,))   #串行操作
        pool.apply_async(func=f1,args=(i,))
    time.sleep(1)
    #pool.terminate()  #当前已经在执行任务（5个）执行完毕,执行一遍立即中止 #立即中止
    pool.close()  #所有任务执行完毕
    pool.join()
    print("end")
