num1 = input("请输入第一个字符串：")
num2 = input("请输入第一个字符串：")
num3 = ''
for i in num1:
    if i not in num2:
        num3 += i

print(num3)

for i in num2:
    num1.replace(i,'')