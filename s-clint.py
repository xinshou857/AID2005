
"""
ftp文件服务客户端
"""
from socket import *

# 服务端地址
ADDR = ("127.70.187.114",8888)

# 实现具体的请求功能
class FTPClient:
    def __init__(self,sock):
        self.sock = sock

    def do_list(self):
        self.sock.send(b"LIST")  # 发送请求
        result = self.sock.recv(128).decode() # 回复 字符串
        # 根据回复分情况讨论
        if result == 'OK':
            # 接收文件列表
            file = self.sock.recv(1024 * 1024).decode()
            print(file)
        else:
            print("文件库为空")

    # 下载文件
    def do_get(self,filename):
        data = "RETR " + filename
        self.sock.send(data.encode()) # 发送请求
        # 等回复
        result = self.sock.recv(128).decode()
        if result == 'OK':
            # 接收文件
            f = open(filename,'wb')
            while True:
                data = self.sock.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
        else:
            print("文件不存在")

def main():
    # 创建套接字
    sock = socket()
    sock.connect(ADDR)

    # 实例化功能类对象
    ftp = FTPClient(sock)

    while True:
        print("============ 命令选项==============")
        print("***           list           ***")
        print("***         get  file        ***")
        print("***         put  file        ***")
        print("***           exit           ***")
        print("==================================")

        cmd = input("请输入命令:")
        if cmd == "list":
            ftp.do_list()
        elif cmd[:3] == "get":
            filename = cmd.split(' ')[-1] # 提取文件名
            ftp.do_get(filename)


if __name__ == '__main__':
    main()