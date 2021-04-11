# from matplotlib import pyplot as plt
# x = range(2,26,2)
# y = [15,13,14.5,17,20,25,26,26,24,22,18,15]
#
# plt.figure(figsize=(10,8),dpi=50)
#
# plt.xticks(x[::1])
# plt.plot(x,y)
# plt.xticks(range(2,20,5))
# # plt.savefig("./temp.svg")
# plt.show()


from matplotlib import pyplot as plt
import random

import matplotlib
matplotlib.rc
x = range(0, 120)

y = [random.randint(20, 35) for i in range(120)]
plt.figure(figsize=(20, 8), dpi=90)
# star = ["*" for i in range(20)]
# print(star)
# print(y)
plt.plot(x, y,)
# plot(lable= "welk")

_xtick_lables = ["10点{}分".format(i) for i in range(60)]
_xtick_lables += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3],_xtick_lables[::3],rotation=90)

plt.show()




















