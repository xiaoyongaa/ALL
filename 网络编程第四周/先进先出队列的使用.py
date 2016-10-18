import queue
#队列，先进先出队列
#put放数据，是否堵塞,阻塞的超时
#
# q=queue.Queue(2)  #队列最大长度2
# print(q.empty())  #判断队列是否为空 空就是true
# q.put(11)  #放进q队列里面11
# q.put(22)
# print(q.empty())
# print(q.maxsize) #队列的最大长度
# #q.put(33,block=False,timeout=2)
# #print(q.qsize())
# print(q.get())  #取出队列里面数据
# print(q.get())
# #print(q.get())
#join,task_done,阻塞竞猜，当队列中任务执行完毕后，不再阻塞
q=queue.Queue(2)
q.put(1)
q.put(2)
q.get()
q.task_done() #你把任务取出来了，告诉一下
q.get()
q.task_done() #你把任务取出来了，告诉一下
q.join() #如果队列里面的任务还没有完成，我就等待着
        #join和task_done一起用
