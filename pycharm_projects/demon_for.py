help(range)
print(range(9))

for i in range(2000):
    print("hello---->", i)
print("*****game over****")

name = '张无忌'
for i in range(1, 6):
    if i == 3:
        print("{}赶快丢掉这个馒头，有毒！".format(name))
    else:
        print("{}很饿，正在吃第{}个馒头。".format(name, i))
print("{}说，终于吃饱了。".format(name))

for i in range(3):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == 'hanhan' and password == '123456':
        print("欢迎回来,{}!".format(username))
        break
    else:
        print("用户名或密码错误。")
else:
    print("登陆次数已经用完，账户被锁定！")
