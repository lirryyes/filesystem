#注意文件名区分大小写,打开操作后，返回文件操作对象，可以利用对象调用read和write方法
try:
    file = open("/Users/liuchun/PycharmProjects/filesystem/README.txt")
except Exception as result:
    print("文件不存在")
    #利用read方法默认是读取文件的所有内容
text = file.read()
print(text)
file.close()