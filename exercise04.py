from multiprocessing import Process,Queue

#创建消息队列
q = Queue()

def request():
    name = 'tom'
    passwd = '123'
    #存入消息队列
    q.put(name)
    q.put(passwd)


def handle():
    #获取消息内容
    name = q.get()
    passwd = q.get()
    print('用户：',name)
    print('密码：',passwd)

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()