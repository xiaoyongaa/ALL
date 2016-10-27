import socket
import contextlib

@contextlib.contextmanager
def conntext_socket(host,port):
    sk=socket.socket()
    sk.bind((host,port))
    sk.listen(5)
    try:
        yield sk
    finally:
        sk.close()


with conntext_socket("127.0.0.1",8888) as sock:
    print(sock)