import matplotlib.pyplot as plt
import numpy as np

# 准备数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制折线图
plt.plot(x, y, label='Sine Wave')

# 特殊节点的位置
special_points = [(3, np.sin(3)), (5, np.sin(5)), (7, np.sin(7))]

# 添加三角形节点
plt.scatter(*zip(*special_points[:1]), marker='^', color='red', label='Triangle')

# 添加五角星节点
plt.scatter(*zip(*special_points[1:2]), marker='*', color='green', label='Star')

# 添加圆圈节点
plt.scatter(*zip(*special_points[2:]), marker='o', color='blue', label='Circle')

# 添加图例
plt.legend()

# 显示图表
plt.show()
