#!/usr/local/python3.5/bin/python3.5
import socket
import sys
def check_port(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
      s.connect((ip,port))
      print (0)
    except Exception:
      print (1)
    s.close()






def run():
    ip=sys.argv[1]
    port=sys.argv[2]
    port=int(port)
    check_port(ip,port)

run()