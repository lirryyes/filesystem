#readline分行读取文件内容，read是一次性读取文件所有内容，将所有内容一次性读取，如果文件太大，对内存占用太大
file = open("/Users/liuchun/PycharmProjects/filesystem/README.txt")
#不知道循环条件的情况下，把循环设置为无限循环
while True:
    text = file.readline()
    if text == "": #或者if not text:
        break
    print(text)
file.close()