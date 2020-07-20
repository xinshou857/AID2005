from socket import *
import time

ADDR = ('127.0.0.1',8008)
class FTPclent:
    def __init__(self,sock):
        self.sock = sock
    def do_list(self):
        self.sock.send(b'LIST')
        result = self.sock.recv(1024).decode()
        if result == 'ok':
            fiel = self.sock.recv(1024).decode()
            print(fiel)
        else:
            print("文件为空")

    def do_get(self, filename):
        data = "RETR " + filename
        self.sock.send(data.encode())  # 发送请求
        # 等回复
        result = self.sock.recv(128).decode()
        if result == 'OK':
            # 接收文件
            f = open(filename, 'wb')
            while True:
                data = self.sock.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
        else:
            print("文件不存在")
    def do_put(self,sunname):
        try:
            f = open(sunname,'rb')
        except FileExistsError:
            print("文件不存在")
        data = 'STOR' + sunname
        #发送请求
        self.sock.send(data.encode())
        #等待回复
        result = self.sock.recv(128).decode()
        if result == "OK":
            #上传文件
            f = open(sunname,'rb')
            time.sleep(0.1)
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sock.send(b'##')
                    break
                self.sock.send(data)

            f.close()
        else:
            print("文件已经存在")


def main():
    sock = socket()
    sock.connect(ADDR)
    ftp = FTPclent(sock)
    while True:
        print("============ 命令选项==============")
        print("***           list           ***")
        print("***         get  file        ***")
        print("***         put  file        ***")
        print("***           exit           ***")
        print("==================================")

        cmd = input("请输入命令：")
        if cmd == 'list':
            ftp.do_list()
        elif cmd[:3] == 'get':
            fielname = cmd.split(' ')[-1]
            ftp.do_get(fielname)
        elif cmd[:3] == 'put':
            sunname = cmd.split(' ')[-1]
            ftp.do_put(sunname)

if __name__ == '__main__':
    main()

