"""
进程池演示
"""
from multiprocessing import Pool
from time import sleep,ctime

def work(msg):
    sleep(2)
    print(ctime(),"__",msg)

pool = Pool(4)

for i in range(10):
    msg = "TEDU%d"%i
    pool.apply_async(func=work, args=(msg,))

pool.close()


