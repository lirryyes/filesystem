class HouseItem:
    '''家具类，该类包括两个属性name 和area'''
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return ( "%s 占地面积 %.2f" %(self.name,self.area) )

#定义房子类，该类包括从外界传过来的两个参数和自身定义的两个参数free_area item_list
class House:
    def __init__(self,huxing,area):
        self.huxing = huxing
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):
        return ("户型：%s\n总面积%.2f【剩余面积：%.2f】\n家具%s"
                %(self.huxing,self.area,self.free_area,self.item_list))
    def add_item(self,item):
         print("添加的家具是%s" %item)
        #1、判断家具的面积
         if item.area > self.free_area:
             print("面积太大，无法摆进房间")
             return
         # 2、将家具的名称添加到列表中,item.name是家具对象的name属性
         self.item_list.append(item.name)
         # 3、计算剩余面积
         self.free_area = self.free_area - item.area




bed = HouseItem("席梦思",34)
chest = HouseItem("衣柜",10)
table = HouseItem("桌子",16)

my_house = House("两房一厅",60)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
print(my_house)