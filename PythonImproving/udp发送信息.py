import socket
def main():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 从键盘获取数据，利用while 循环发送
    while True:
        nei = input("请输入内容：")
        #如果输入内容为exit 则退出循环
        if nei == "exit":
            break
    #套接字发送数据，发送数据没有指定端口，操作系统会随机给程序随机分配一个端口（动态端口）
        udp_socket.sendto(nei.encode("utf-8"),("10.1.163.190",8989))
    udp_socket.close()
if __name__ == "__main__":
    main()