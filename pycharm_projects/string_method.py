import random
msg = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
code = ''
for i in range(4):
    ran = random.randint(0,len(msg)-1)
    code += msg[ran]
print('验证码是：',code)
user_input = input("请输入验证码：")
if user_input.lower() == code.lower():
    print("验证成功！"
          )
else:
    print("验证失败！")
