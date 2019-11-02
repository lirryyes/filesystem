class Women:
    def __init__(self,name):
        self.name = name
        self.age = 10
    def __secret(self):
        print("%s 的年龄是 %d" % (self.name,self.__age))

xiaofang = Women("小芳")
#__age为私有属性不能在类外部调用，因此运行程序时会报错
print(xiaofang.__age)
#____secret为私有方法不能在类外部调用，因此运行程序时会报错
print(xiaofang.__secret)