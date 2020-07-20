from socket import *
from threading import Thread
import os,time
HOST = '0.0.0.0'
PRIT = 8008
ADDR = (HOST,PRIT)

FTP = '/home/tarena/ETP/'

class FTPserver(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    def do_list(self):
        sun = os.listdir(FTP)
        if not sun:
            self.connfd.send(b'FAIL')
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)
            data = '\n'.join(sun)
            self.connfd.send(data.encode())

    def do_get(self,fielname):
        try:
            f = open(FTP+fielname,'rb')
        except:
            self.connfd.send(b'FAIL')
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
            while True:
                data = f.read(1024)
                if not  data:
                    time.sleep(0.1)
                    self.connfd.send(b"##")
                    break
                self.connfd.send(data)
            f.close()

    def do_put(self,sunname):
        if os.path.exists(FTP+sunname):
            self.connfd.send(b"FAIL")
            return
        else:
            self.connfd.send(b"OK")
            f = open(FTP + sunname, 'wb')
            while True:
                data = self.connfd.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if data == 'LIST':
                self.do_list()

            elif data[:4] == 'RETR':
                fielname = data.split(' ')[-1]
                self.do_get(fielname)

            elif data[:4] == 'STOR':
                sunname = data.split(' ')[-1]
                self.do_put(sunname)
        self.connfd.close()


def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %s"%PRIT)
    while True:
        try:
            connfd,addr = sock.accept()
            print("Conming from",addr)
        except KeyboardInterrupt:
            sock.close()
            return

        t = FTPserver(connfd)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()


