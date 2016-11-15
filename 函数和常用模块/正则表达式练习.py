import re
with open("haproxy.cnf.txt","r") as db:
    db=db.read()


r=re.sub("server 100.1.7.9 .* weight .* maxconn .*","server 100.1.7777.9  100.1.7777.9 weight 2000 maxconn 333",db)
print(type(r))
with open("r.txt","w") as e:
    for i in r:
        e.write(i)



