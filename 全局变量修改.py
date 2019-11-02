#在一个函数中对全局变量进行修改时，到底是否需要使用global进行说明要看是否对全局变量的指向进行了修改，如果修改了指向
# ，即让全局变量指向了一个新的地方，那么必须使用global 如果仅仅是修改了指向的空间中的数据，此时不用必须使用global
num = 100
nums = [1,2]
def test1():
    global num
    num += 100 #改变指向
def test2():
    nums.append(3)#改变指向空间的值
test1()
test2()
print(num)
print(nums)


