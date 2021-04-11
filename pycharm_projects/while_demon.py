n = 1
while n <= 30:
    if n%3 == 0:
        print(n)
    n +=1


n = 3
while n <= 30:
    n +=3



num = 1
sum = 0
while num <= 20:
    sum += num

    num = num +1

#打印三角形尝试
i = 0
while i <= 20:
    print("*"*i)
    i +=1


floor = 1
while floor <= 50:
    count = 1
    while count <= floor:
        print("*",end='')
        count +=1
    floor += 1
    print()

floor = 1
while floor <= 9:
    count = 1
    while count <= floor:
        print("{} * {} = {}    ".format(count,floor,floor*count),end="")
        count += 1
    floor += 1
    print()








