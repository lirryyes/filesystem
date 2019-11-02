class Cat:
    def __init__(self):
        self.name = "tom"
        print(self.name)
    def eat(self):
        print("%s 小猫爱喝水" % self.name)
    def drink(self):
        print("小猫爱吃鱼")
    def __del__(self):
        print("此步执行将销毁对象")

Tom = Cat()
print(Tom)
Tom.eat()
#__del__将在程序执行完最后一个方法Tom.eat()后进行调用，目的是自动销毁Tom对象