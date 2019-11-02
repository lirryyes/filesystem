def demo(num,num_list):
    num += num
    num_list += num_list
    print("%s %s" %(num,num_list))
glo_num =2
glo_num_list = [4,5,6]
demo(glo_num,glo_num_list)
print("%s %s" %(glo_num,glo_num_list))