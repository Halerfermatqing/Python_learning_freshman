print('*'*10,'欢饮来到消消乐','*'*10)
level = input("请输入你的级别（lv1，lv2）")
if level == 'lv1':
    print('免费玩，随便玩')
else:
    print("已近进入付费级别，充值继续玩")
    money = int(input("请充值（充值金额必须是100的倍数）"))
    if money%100 == 0 and money > 0:
        print('充值成功！充值金额是：',money)
    else:
        print("充值失败，充值金额必须是100的倍数！")


import random
ran = random.randint(1,10)
num = input("请输入（1-10）之间的随机数：")
if ran == int(num):
    print("恭喜中大奖了！奖品是：笔记本")
else:
    print("很遗憾你猜错了！与奖品擦肩而过~~~~~~")
