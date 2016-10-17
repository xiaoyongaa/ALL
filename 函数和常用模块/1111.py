import hashlib
password="2"
jiami=hashlib.md5(bytes("d312",encoding="utf-8"))

jiami.update(bytes(password,encoding="utf-8"))  #保存的对象加密密码
password=jiami.hexdigest()  #成功加密密码
print(password)