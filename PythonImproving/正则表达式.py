import re
#匹配单个字符[1-8]匹配1到8的数字 ；【1-26-8】1到2 6到8中的一位数字；【13478】匹配134678中的一位
#【123rty】匹配123rty中的任何一位
#\w表示匹配a-z A-z 0-9 _(下划线)、中文、日文、英文（返回太广了请慎用）
ret1 = re.match("速度与激情[1-8]","速度与激情e22")
#匹配0到9的任意一个数字
ret2 = re.match("速度与激情\d","速度与激情2")
#匹配多个字符\d{1,3} 匹配1到3位的数字；\d{11}必须匹配11位数字
print(ret1)#匹配到了就返回匹配到的值，匹配不到就返回none
#电话号码020-90909090,  解释，-？表示-有一个或者没有
ret3 = re.match("\d{3,4}-?\d{7,8}","02109456345")
#如果执行上面一句报错AttributeError: 'NoneType' object has no attribute 'group' 该报错表示没有匹配上，返回为空，空变量没有group方法
b = ret3.group()
print(b)
#.*匹配任意多个字符，除了换行外,点表示任意一个字符除了换行\n
# test = """oio
# # kjkj
# # kjgkd"""  #三个双眼号之间是字符串，可以实现字符串换行
test ="34\n0inj\n"  #\n也是一种换行方式
print(test)
ret4 = re.match(r".*",test).group()
ret5 = re.match(r".*",test,re.S).group() #多一个参数re.S,可以匹配到换行
#+和*类似，只不过
print(ret5)