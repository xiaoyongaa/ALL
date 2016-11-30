infor=[{"user":"x","passd":1},{"user":"r","pass":2}]
for i in infor:
    print(i.get("user"))
    if "r" in i.get("user"):  #r用户在文件内
        print("存在这个用户")
    else:
        print("不存在这个用户")

