import time
import threading

# """没有使用多任务，sing和dance顺序执行，不能并行"""
# def sing():
#     for i in range(0,5):
#         print("正在唱歌。。")
#         time.sleep(1)
#
# def dance():
#     for i in range(0,5):
#         print("正在跳舞。。")
#         time.sleep(1)
#
# def main():
#     sing()
#     dance()
#
#
# if __name__ == '__main__':
#     main()

"""使用多任务处理，让sing和dance并行执行"""
def sing():
    for i in range(0,50):
        print("正在唱歌。。")
        time.sleep(1)

def dance():
    for i in range(0,50):
        print("正在跳舞。。")
        time.sleep(1)

def main(): #main函数为主线程,主线程结束，整个程序才结束
    t1 = threading.Thread(target=sing) #t1为Thread的实例对象
    t2 = threading.Thread(target=dance)
    t1.start()#启动线程，此时线程才生成
    t2.start()
    for i in range(50):
        print(threading.enumerate())
        time.sleep(2)

if __name__ == '__main__':
    main()