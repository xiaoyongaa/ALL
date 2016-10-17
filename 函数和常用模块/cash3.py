import re
a="2+1+3+3123123"
r=re.findall(r"\d{0,}[\+\-]{0,}",a)
print(r)
with open("re.txt","w") as re:
    for i in r:
        re.write(i)
with open("re.txt","r") as r:
    r=r.read()
print(r)