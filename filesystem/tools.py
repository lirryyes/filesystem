cards = []
def show_all():
    print("欢迎使用【名片管理系统】")
    print("1、新增名片")
    print("2、显示全部")
    print("3、搜索名片")
    print("4、退出系统")
    print("*" * 20)
    print("请选择您好进行的操作：")
def add_cards():

    name = input("姓名")
    phone = input("电话：")
    qq = input("扣扣：")
    email = input("邮箱：")

    cards_dict = {"name":name,
                  "phone":phone,
                  "qq":qq,
                  "email":email,
    }
    cards.append(cards_dict)
    return  cards
def show_cards():
    print("姓名\t\t 电话\t\t 扣扣\t\t 邮箱\t\t")
    for i in cards:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" %(i["name"],i["phone"],i["qq"],i["email"]))
def search_cards():
    print("请输入要搜索的人员姓名")
    search_name = input()
    for cards_dict in cards:
        if search_name == cards_dict["name"]:
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (cards_dict["name"],
                                                cards_dict["phone"],
                                                cards_dict["qq"],
                                                cards_dict["email"]))
            break
    else:
        print("输入名字不存在")

