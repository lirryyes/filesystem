
card_list = []
def show_menu():
    print("*" * 20)
    print("欢迎使用【名片管理系统】V1。0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 20)

def new_card():
    print("新增名片")
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入扣扣：")
    email = input("请输入email：")
    card_dict = {
        "name":name,
        "phone": phone,
        "qq":qq,
        "email":email
    }
    card_list.append(card_dict)
    print(card_list)

def show_all():
    print("-" * 20)
    print("显示所有名片")
    if len(card_list) == 0:
        print("暂无名片")
        return #return后面没有任何内容时候返回调用函数的位置，return下方的内容不再执行
    for name in ["姓名","电话","QQ","邮箱" ]:
        print(name,end="\t\t")
    print("")
    #遍历名片列表，输出名片内容
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" %(card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))

def search_card():
    print("搜索名片信息")
    find_name = input("请输入要搜索的名片姓名：")
    for card_dict in card_list:
        if card_dict["name"] ==find_name:
            print("%s\t\t%s\t\t%s\t\t%s\t\t" %(card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("无")
def deal_card(find_dict):
    """对名片进行修改和删除操作

    :param find_dict:
    """
    action_str = input("请选择要执行的操作"
                       " [1]修改 [2]删除 [0]返回上级菜单")
    #修改名片
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"],"姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"],"扣扣：")
        find_dict["email"] = input_card_info(find_dict["email"],"邮箱：")
    #删除名片
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除 %s 成功" % find_dict["name"])
def input_card_info(dict_value,tip_message):
    """修改名片，如果不做任何修改则返回原有字典值

    :param dict_value:
    :param tip_message:
    :return:
    """
    #提示用户输入内容
    resul_str = input(tip_message)
    #针对用户输入进行判断，如果用户输入了内容，直接返回输入的内容
    if len(resul_str) > 0:
        return resul_str
    #如果用户没有输入内容，返回字典原有值
    else:
        return dict_value

