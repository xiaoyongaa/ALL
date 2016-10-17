#!/app/python3.5/bin/python3.5
import os
r=os.system("df -h | awk 'BEGIN{FS=\" \"}{print$5}' |sed 's/%//g'| grep -v Use")
e=os.popen("df -h | awk 'BEGIN{FS=\" \"}{print$5}' |sed 's/%//g'| grep -v Use").read()
print(r)
if r==0:
    print("ok")
    wenjian=open("a.txt","w")
    wenjian.write(e)
    wenjian.close()
    all_open=open("a.txt","r")
    all_open=all_open.read()
    for i in all_open:
        i=int(i)
        if i>=60:
           print("baojing")
        else:
           print("zhengchang")
