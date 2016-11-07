import socket
import select
ip_port=("127.0.0.1",9999)
sk=socket.socket()
sk.bind(ip_port)
sk.listen(5)
inputs=[sk,]
outputs=[]
while True:
    rlist,wlist,e=select.select(inputs,outputs,[],1)
    print(len(inputs),len(rlist),len(wlist))
    for r in rlist:        #循环的去rlist里面去取sk对象，并且accept连接
       if r==sk:
           conn,addr=r.accept()
           inputs.append(conn)
           conn.sendall(bytes("hello",encoding="utf-8"))
       else:
            try:
                ret=r.recv(1024)
                if not ret:
                    raise Exception("断开连接")
                else:
                    outputs.append(r)
            except Exception as ex:
               inputs.remove(r)
    for w in wlist:
         w.sendall(bytes("re",encoding="utf-8"))
         outputs.remove(w)

'''
rlist中就是socket对象列表
'''