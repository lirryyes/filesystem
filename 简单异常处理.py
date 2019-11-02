try:
    #不能确定正确执行的代码
    num = int(input("请输入整数："))
except:
    #try出现错误后跳到此处执行此处代码
    print("请输入正确的数字")
print("-"*50)