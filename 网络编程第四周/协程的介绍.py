# #协程
# '''
# IO密集型-多线程   协程来做更好
# 计算密集型-多进程
#
# '''
# #协程
#
# 原理：只利用一个线程，分解一个线程为多个为微线程
# #greenlet 底层的
# #gevent封装好的直接用
# from gevent import monkey; monkey.patch_all()
# import gevent   #协程
# import requests
import sys
import requests

#import gevent

url="http://www.cnblogs.com/wupeiqi/articles/5040827.html"
#
def f(url):
    #print('GET: %s' % url)
    resp=requests.get(url)
    #res=resp.status_code  #返回http狀態
    data=resp.text
    data=bytes(data,encoding="utf-8")
    print(type(data))
    with open("E:\\test.html","wb") as new:
       new.write(data)


    #print(resp.text)


f(url)
#
# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'https://github.com/'),
# ])




