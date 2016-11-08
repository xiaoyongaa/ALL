from multiprocessing import  Pool
import time
def f1(arg):
    time.sleep(1)
    print(arg)

if __name__=="__main__":
    pool=Pool(5)
    for i in range(30):
        pool.apply_async(func=f1,args=(i,))
    #print("end")
    #pool.close()  #所有任务执行完毕
    # time.sleep(1)
    # pool.terminate()  #立即中止
    #pool.join()

