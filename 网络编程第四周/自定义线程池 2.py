#线程只能创建这么多，再创建就不行了。
import threadpool
import time
def task(a):
    print(a)


pool=threadpool.ThreadPool(2)
res=threadpool.makeRequests(task,args_list=["11",])
for i in  res:
    pool.putRequest(i)

pool.wait()



