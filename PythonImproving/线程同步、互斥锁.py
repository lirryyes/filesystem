import threading

glo_nums = 0
mutex = threading.Lock()
def test1(temp1):
    global glo_nums
    for i in range(temp1):
        mutex.acquire()#加锁，被锁的代码越少越好
        glo_nums += 1
        mutex.release()#释放锁
    print(glo_nums)

def test2(temp2):
    global glo_nums
    for i in range(temp2):
        mutex.acquire()
        glo_nums += 1
        mutex.release()
    print(glo_nums)


def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()