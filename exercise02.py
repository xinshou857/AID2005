from  threading import Thread
from socket import *

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)


def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not  data:
            break
        print("recv:",data.decode())
        connfd.send(b'who are you')
    connfd.close()
def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %s"%PORT)
    while True:
        try:
            connfd,addr = sock.accept()
            print("Connter from",addr)
        except:
            sock.close()
            return
        p = Thread(target=handle,args=(connfd,))
        p.setDaemon(True)
        p.start()

if __name__ == '__main__':
    main()