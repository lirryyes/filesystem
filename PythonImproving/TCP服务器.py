import  socket
def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #插入手机卡（绑定本地信息 bind）
    a = ("",7890)
    tcp_server_socket.bind(a)
    #将手机设置为正常的响铃模式（让默认的套接字由主动变成被动listen）
    tcp_server_socket.listen(128)
    print("--1--")
    #等待别人的电话到来（等待客户端链接，accept）
    new_client_socket,client_addr = tcp_server_socket.accept()
    print("---2---")
    print(client_addr)
    #接受客户端发送过来的请求
    recv_data = new_client_socket.recv(1024)
    print(recv_data)
    #回松一条信息给客户端
    new_client_socket.send("已经收到".encode("utf-8"))
    new_client_socket.close()
    tcp_server_socket.close()
if __name__ == "__main__":
    main()