from multiprocessing import Pool,Queue
import os,sys

q = Queue()
def copy(file,old_file,new_file):
    item = open(old_file+'/'+file,'rb')
    item02 = open(new_file+'/'+file,'wb')
    while True:
        data = item.read()
        if not data:
            break
        n = item02.write(data)
        q.put(n)
    item02.close()
    item.close()
def get_size(dir):
    total_size = 0
    for file in os.listdir(dir):
        total_size += os.path.getsize(dir + '/' + file)
    return total_size
def main():
    old_file = input("请输入拷贝的文件目录：")
    new_file = old_file + '-备份'
    total_size = get_size(old_file)
    try:
        os.mkdir(new_file)
    except:
        sys.exit('该目录已经存在')

    pool = Pool()
    for file in os.listdir(old_file):
        pool.apply_async(func=copy,args=(file,old_file,new_file))

    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get()
        print('拷贝了%.1f%%'%(copy_size/total_size*100))
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()