import random
print("*"*30)
print("欢迎来到澳门赌场！")
print("*"*30)
username = input("请输入你的名字：")
money = 0
answer = input("确定是否进入游戏吗？（y/n）")
if answer == 'y':
    #判断用户游戏币是否充足
    while money <2:
        n = int(input("金币不足，请充值，必须是100的倍数"))
        if n % 100 == 0:
            money = (n//100) * 30
    print("当前剩余游戏币是：{}，玩一局扣除两个币".format(money))
    input("是否进入游戏？（y/n）")
    if answer == "y":
        while True:
            print('进入游戏。。。。。')
            t1 = random.randint(1,6)
            t2 = random.randint(1, 6)

            print("系统洗牌完毕，请猜大小：")
            guess = input("请输入大或小")

            if ((t1+t2) > 6 and guess == "大") or (t1+t2) <= 6 and guess == "小":
                print("恭喜你，游戏币加一")
                money += 1
                answers = input("要再来一次吗？（y/n）")
                if answers == 'n':
                    break
            else:
                answers = input("要再来一次吗？（y/n）")
                if answers == 'n':
                    break

    else:
        print("退出游戏！！！！！！")