import  threading
# glo_nums = [1,2]
glo_nums =100
def test1(temp1):
    # temp1.append(100)
    temp1 +=100
    print(str(temp1))
def test2(temp2):
    print(str(temp2))
def main():
    t1 = threading.Thread(target=test1,args=(glo_nums,))  #args为元组类型的参数
    t2 = threading.Thread(target=test2, args=(glo_nums,))
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()
