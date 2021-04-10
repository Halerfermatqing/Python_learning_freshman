age = 18
print('年龄是：%s'%(age))

#age = 18    TypeError: can only concatenate str (not "int") to str
#print('年龄是：' + age)

age = 18
print('年龄是：' + str(age))
print("结婚否？回答%s" % (False))
print("年龄是%2d" % age)

age = 19.83741872348
print("年龄是%.4f" % age)

#练习
movie= '大侦探皮卡丘'
ticket = 45.9
count = 35
print("""电影：%s
人数：%d
单价：%f
总票价：%.1f""" % (movie,count,ticket,ticket*count))

name = "乔治"
age  = 3
hobby = "玩恐龙"
msg = "{}今年{}岁，最喜欢玩{}".format(name,age,hobby)
print(msg)