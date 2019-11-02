#主动抛出异常
#提示用户输入密码，如果长度小于8则抛出异常，如果长度大于等于8不抛出异常
def demo():
    print("请输入密码：")
    password = input("")
    num = len(password)
    print(num)
    if num >=8:
        return password
    #ex为人为定义的异常
    ex = Exception("密码长度不够")
    #利用raise主动抛出异常
    raise  ex
try:
    demo()
    #进行异常捕获，此处抛出的异常就为程序定义的异常
except Exception as e:
    print(e)