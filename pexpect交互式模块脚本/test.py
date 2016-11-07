import psutil
mem=psutil.virtual_memory()
print(mem.total/1024/1024/1024)  #默认是字节B