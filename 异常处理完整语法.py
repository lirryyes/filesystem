#捕获未知错误
try:
    #try里面的代码是尝试被执行的代码
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
    #如下except为已经异常
except ValueError:
    print("输入正确的整数")
    #如下except为未知异常
except Exception as result:
    print("未知错误%s" %result)
else:
    print("尝试执行没有错误时候被执行")
finally:
    print("无论是否出现错误都会被执行")
print("-"*80)