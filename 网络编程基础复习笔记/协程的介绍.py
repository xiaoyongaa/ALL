'''
原理：利用一个线程，分解一个线程成为多个微线程
'''

import greenlet
import gevent
import requests

def run(url):
    res=requests.get(url)
    data=res.text
    print(len(data),res.url)


gevent.joinall([gevent.spawn(run,"http://edu.51cto.com/?www"),gevent.spawn(run,"http://www.qq.com"),gevent.spawn(run,"http://www.baidu.com"),])


