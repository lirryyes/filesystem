from filesystem import tools
while True:
    tools.show_all()
    a = input()
    if a == "1":
        tools.add_cards()
    elif a == "2":
        tools.show_cards()
    elif a == "3" :
        tools.search_cards()
    # elif (a !=1 and a!=2 and a!=3 and a!=4):
    #     print("您输入有误，请重新输入")
    #     pass
    elif a == '4':
        break
    else:
        print("输入有误，请重新输入")