#递归函数特点：自己调用自己
#递归函数一定要有递归出口：当参数满足某个条件时，不再执行函数

def sum_numbers(num):
    if num == 1:
        return 1
    temp = sum_numbers(num-1)
    return(num+temp)

print(sum_numbers(3))