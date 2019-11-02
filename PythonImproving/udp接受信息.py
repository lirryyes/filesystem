import socket


def main():
    # 创建套接字
    udp_scoket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定一个本地信息
    localaddr = ("", 7788)  # ip地址不填写表示本地IP或者是任意IP
    udp_scoket.bind(localaddr)
    # 接受数据
    while True:
        recv_data = udp_scoket.recvfrom(1024)
        # 打印信息，打印的信息为一个元祖(b'2', ('10.1.163.190', 8989))
        a = recv_data[0]  # a来接受发送的信息
        b = recv_data[1]  # b来接受发送方的IP和端口
    # 当发送信息为中文时候，打印a会出现乱码，因为网络调试工具发送的是gbk编码后的，所以这里要进行解码
        print("%s %s" % (a.decode("gbk"), str(b)))
    udp_scoket.close()


if __name__ == "__main__":
    main()
