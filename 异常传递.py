def demo1():
    num = int(input("请输入整数："))
def demo2():
    demo1()
# try:
#     demo2()
# except Exception as result:
#     print("输出异常：%s" %result)
#如下demo2()调用称为主函数，主函数调用demo2 demo2又调用demo1所以demo1处的异常先传递给demo2 然后再传递给主函数
#所以异常只需要在主函数进行处理即可，不用在每一个函数内部进行异常处理
demo2()