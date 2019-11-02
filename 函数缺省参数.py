def demo(name,title='q',gender=True):
    gender_a ='男生'
    if not gender:
        gender_a = '女生'
    print("%s %s %s" %(name,title,gender_a))

demo('晓鸣','yy') #输出晓鸣 女生
demo('xiaomei',gender=False) #输出xiaomei 男生
#带有默认值的缺省参数应该放在参数列表的末尾
#如果有多个缺省参数，需要指明传给哪个默认参数