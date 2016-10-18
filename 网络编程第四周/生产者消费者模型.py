import queue
q=queue.Queue(20)


def productor():
    q.put("包子")



def connsumer():
    q.get()



