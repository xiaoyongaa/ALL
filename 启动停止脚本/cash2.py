
def  cheack_port():
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
try:
    s.connect((ip,port))
    #print(0)
    count=1
 except Exception:
    count+=1
    os.chdir(path)
    count=str(count)
    os.system("echo"+" "+count+" "+"&>cishu.txt")
    count=int(count)
 s.close()