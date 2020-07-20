from  multiprocessing import  Pool
from  time import sleep,ctime

#如果父进程结束，进程池自动销毁
#进程池执行事件
def worker(msg,sec):
    print(ctime(),'-----',msg)
    sleep(sec)

#创建进程池
pool = Pool(4)

#向进程池加入事件
for i in range(10):
    msg = 'tedu-%d'%i
    pool.apply_async(func=worker,args=(msg,2))#事件可以开始执行

pool.close()#关闭进程池，不能添加新的事件
pool.join()