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

import gevent
print(sys.path)
# url="https://www.python.org/"
#
# def f(url):
#     #print('GET: %s' % url)
#     resp = requests.get(url)
#     res=resp.status_code  #返回http狀態
#     data = resp.text
#     print(url,res)
#     #print(resp.text)


f(url)
#
# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'https://github.com/'),
# ])




