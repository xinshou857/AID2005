from  multiprocessing import Process
import time


def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("执行时间：",end_time - start_time)
        return res
    return wrapper

# @timeis
# def fun():
#     pn = []
#     for i in range(100001):
#         if i <= 1:
#             continue
#         else :
#             # 有非1非本身因子即中断循环
#             for j in range(2,i):
#                 if i % j == 0:
#                     break
#             else:
#                 pn.append(i)
#     print(sum(pn))
# p = Process(target=fun)

def sun():
    pn = []
    for i in range(1,100001,25000):
        if i <= 1:
            continue
        else :
            # 有非1非本身因子即中断循环
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                pn.append(i)
    print(sum(pn))
s = Process(target=sun)
# p.start()
#
# p.join()

s.start()
s.join()