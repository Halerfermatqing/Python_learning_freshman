print("""
******************************
            捕鱼达人
******************************""")
username = input('请输入参与者用户名：')
password = input("请输入密码：")

print("%s请充值才能加入游戏！"% username)

coins = input("请充值：")
print("%s 充值成功，当前游戏币是：%s" %(username,coins))