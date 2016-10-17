import socket
import selectlist,wlist,errorlist=select.select(inputs,outputs,[],1)
    print(len(inputs),len(rlist),len(wlist))
    #监听SK(服务端)对象，如果SK发生变化，表示有客户端来连接了。此时rlist值为sk
    #监听conn对象，如果conn发生变化，表示客户端发消息过来了。此时的rlsit为客户端
    #print(rlist)
ip_port=("127.0.0.1",9999)
sk=socket.socket() #创建sockeet对象
sk.bind(ip_port)  #绑定电话卡
sk.listen(5)   #开机等待电话
#conn,addr=sk.accept()  #创建链接对象  conn是客户端链接对象
inputs=[sk,]  #select当前监听了几个对象
outputs=[]   #发过消息的用户对象集合
messages={}
while True:
    r
    #rilist中socket对象列表
    #rlist=[sk]
    for r in rlist:
        if r==sk:  #如果r是sk，就说明是新连接，创建新连接
            conn,addr=r.accept()
            conn.sendall(bytes("hello",encoding="utf-8"))
            inputs.append(conn)
            messages[conn]=[]
        else:
            try:
                #有人给我发消息了
                shou=r.recv(1024)
                if len(shou)==0:  #接收空内容的时候,也会断开，移除该链路的对象
                    inputs.remove(r)
                    raise Exception("djkaskdj")
                else:
                    outputs.append(r)
                    messages[r].append(shou)
            except Exception as ex:   #客户端断开的时候，移除该链路的对象
                print(ex)
                inputs.remove(r)
                del messages[r]
    #所有给我发过消息的人
    for w in wlist:
        msg=messages[w].pop()
        msg=str(msg,encoding="utf-8")
        new="测试{n}".format(n=msg)
        outputs.remove(w)  #发过消息后，要移除掉对象







        w.sendall(bytes(new,encoding="utf-8"))


