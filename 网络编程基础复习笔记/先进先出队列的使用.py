import queue
q=queue.Queue(2)
#print(q.empty())
q.put(11)
q.put(22)
#q.put(111,block=False)
#print(q.qsize())
#print(q.empty())  #判断队列是否为空
print(q.full())
print(q.get())
print(q.get())
print(q.get(block=False))