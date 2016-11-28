host_list=[{"host":"192.168.10","username":"root","port":"22","password":"123"},
           {"host":"192.168.11","username":"root","port":"22","password":"113"},
           {"host":"192.168.12","username":"root","port":"22","password":"103"},
           ]

for key,i in enumerate(host_list,1):
    print(key,i)

mun=int(input("请输入你要选择的主机:"))
try:
    infor=host_list[mun-1]
    print(infor)
    username=infor.get("username")
    hostname=infor.get("host")
    password=infor.get("password")
    print(username,hostname,password)

except Exception as ex:
    print(ex)

