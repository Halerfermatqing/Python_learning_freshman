import matplotlib.pyplot as plt
squres = [1,4,9,16,25]
input_values = [1,2,3,4,5]
plt.plot(input_values,squres,linewidth=5,)
#设置图表标题，并给坐标轴加上标签，设置字体大小为14
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的字体大小为14，便于阅读
plt.tick_params(axis="both", labelsize=14)
plt.show()