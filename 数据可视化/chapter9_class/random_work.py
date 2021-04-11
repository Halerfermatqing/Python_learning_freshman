from random import choice
class Randomwork():
    """"生成一个随机漫步的数据的类"""

    def __init__(self, num_points = 5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

    #所有的随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有的点"""

        #不断漫步，直到达到列表长度
        while len(self.x_values) < self.num_points:
            #决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4,]) #加上0是为了可以沿着y轴移动
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4,]) #加上0是为了可以沿着x`轴移动
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)






