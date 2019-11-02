import threading
import time

class myThread(threading.Thread):
    def run(self): #run方法一定要有
        for i in range(5):
            print(self.name)
            self.login()
    def login(self):
        print("这是登录模块")

if __name__ == "__main__":
    t = myThread()
    t.start()#注意这里不是直接调用run方法，直接调用start方法，然后会自动调用run方法