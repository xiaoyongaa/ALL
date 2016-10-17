import socket
def check_port():
    ip="127.0.0.1"
    port=int(9309)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
      s.connect((ip,port))
      print (0)
    except Exception:
      print (1)
    s.close()

check_port()