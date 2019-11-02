from multiprocessing import Pool
import time
import os

def work(arg):
    stat_time = time.time()
    print("执行work函数%s" %(os.getpid()))
    time.sleep(3)
    stop_time = time.time()
    print("%s 执行时间为 %s" %(arg,stop_time-stat_time))

pool = Pool(3) #创建线程数量为3的线程池
for i in range(0,10):
    pool.apply_async(work,(i,))
print("----1--")
pool.close() #先close然后再调用join，告知主程序已经执行完毕pool执行完毕，zhuchengxu
pool.join() #join的作用是，主程序会停留在此处等待线程池里面的线程执行完毕，主程序再继续往下执行print("----2--")
print("----2--")
