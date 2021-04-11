import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value, y_value, s=40, edgecolors="none",c=y_value, cmap=plt.cm.Blues)

# 设置图表标题并且给坐标轴加上标签
plt.title("Square Number", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of values", fontsize=14)

# 设置标记刻度的字体大小
plt.tick_params(axis="both", labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.savefig("squares_plot.png", bbox_inches = "tight")
plt.show()
