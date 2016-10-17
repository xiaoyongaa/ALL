#!/app/python3.5/bin/python3.5
import os
r=os.system("df -h | awk 'BEGIN{FS=\" \"}{print$5}' |sed 's/%//g'| grep -v Use")
e=os.popen("df -h | awk 'BEGIN{FS=\" \"}{print$5}' |sed 's/%//g'| grep -v Use").read()
print(r)
if r==0:
    print("ok")
    l=list(e)
    print(l)
    count=l.count("\n")
    print(count)
    for i in range(count):
        i=int(i)
        if i==1:
            y=l.index("\n")
            d=l[0:y]