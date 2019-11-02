#捕获错误类型,针对错误类型捕获异常
#提示用户输入整数
try:
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
except ZeroDivisionError :
    print("除0错误")
except ValueError:
    print("输入整数错误")
#有多少种错误类型就把多少种错误类型添加在except后面