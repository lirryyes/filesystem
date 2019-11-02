class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0
    def add_bullet(self,count):
        #获取count参数来修改抢的子弹数量
        self.bullet_count += count
    def shoot(self):
        #1、判断子弹数量
        if self.bullet_count <= 0:
            print("没有子弹，无法发射")
            return
        # 2、发射子弹，-1
        self.bullet_count -=1
        print("子弹已经发射，%s剩余子弹数量%d" %(self.model,self.bullet_count))
        #3、提示发射子弹信息

class Soldier:
    def __init__(self,name):
        self.name = name
        #每个士兵刚开始都没有抢，如果不知道初始值赋予什么值，建议用none进行赋值，所以不需要给gun传递形参
        self.gun = None
    def fire(self):
        if self.gun == None:
            print("没有枪，无法开枪")
            return
        print("预备装子弹开枪")
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("AK47")
# ak47.add_bullet(50)
# ak47.shoot()

#创建士兵对象
xusanduo = Soldier("徐三多")
#在类内部设置gun属性，在类外部给这个gun属性赋值
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)