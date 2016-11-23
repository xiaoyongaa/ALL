from multiprocessing import Pool
import time


def f1(arg):
    time.sleep(1)
    print(arg)


if __name__=="__main__":
    pool=Pool(5)
    for i in range(30):
        #pool.apply(func=f1,args=(i,))
        pool.apply_async(func=f1,args=(i,))  #同时执行
    time.sleep(1)
    pool.terminate() #只执行5个任务

    #pool.close()  #30个任务执行完毕
    pool.join()  #join方法前面要断言 必须执行close方法或者terminate
    print("end")