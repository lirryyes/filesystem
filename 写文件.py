#w、a都是以写的方式打开文件，w会覆盖原来文件里面的内容，a会是把写入的内容追加到文件末尾
file = open("/Users/liuchun/PycharmProjects/filesystem/README.txt","a")
file = open("/Users/liuchun/PycharmProjects/filesystem/README.txt","w")
file.write("hello")
file.close()