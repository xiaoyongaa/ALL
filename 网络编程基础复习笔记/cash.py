# n=[]
#
# try:
#     if len(n)==0:  #判断n是不是为空
#         raise Exception("dssda")
# except Exception as ex:
#         print(ex)


msg={}

conn=1
msg[conn]=[]
msg[conn].append(2222)
e=msg[conn].pop()
print(e)
print(msg)


