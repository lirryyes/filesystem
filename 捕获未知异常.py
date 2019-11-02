#捕获未知错误
try:
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("输入正确的整数")
except Exception as result:
    print("未知错误%s" %result)
    #输出未知异常result