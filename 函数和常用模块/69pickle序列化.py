import pickle
import json
'''li=[11,22,33]
li=pickle.dumps(li)
print(type(li))
print(li)
re=pickle.loads(li)
print(type(re))
print(re)
'''
'''
ls=[1,2,3]
pickle.dump(ls,open("tt","wb"))   #写进一个文件
re=pickle.load(open("tt","rb"))
print(re)
'''
k='{"k":123}'
print(type(k))
k=pickle.dumps(k)
print(type(k))
print(k)
k=pickle.loads(k)
print(type(k))
print(k)


import pickle
date={"1":"2","2":"2","3":"32213"}
pickle.dump(date,open("pk.txt","wb"))
p=pickle.load(open("pk.txt","rb"))
print(p)




#k=pickle.loads(k)
#pickle.dump(li,open("db","wb"))

#li=pickle.loads(k)
#print(k)
#print(type(k))
