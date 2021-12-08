#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

'''
Pyplot 是 Matplotlib 的子库，提供了和 MATLAB 类似的绘图 API。让用户绘制 2D 图表.
subplots():可以在一张图片上绘制一个或多个图表
scatter():绘制单个点，将向它传递一对xy坐标
ax.set_title:给子图设置标题
tick_params:设置刻度标记
plt.style.use：设置子表背景
fig.autofmt_xdate():绘制倾斜的X轴坐标，避免其彼此重叠
edgecolors='none':删除每个点周围的轮廓

1. 绘制简单的散点图,修改标签文字和线条粗细，校正图形，使用内置样式，自定义数据点颜色/使用颜色映射
   自动保存图表
2. 坐标值随机，自动计算数据
'''
# x,y轴的值
x_values = [i for i in range(100)]
y_values = [i**2  for i in range(100)]

plt.style.use('ggplot')                                                   # 使用内置样式，设置子表背景
fig,ax = plt.subplots()                                                   # 变量fig表示整张图片，变量ax表示图片中的各个图表

# ax.scatter(x_values,y_values,s=5,color=(0,0.8,0))                       # s表示点的大小，color是三原色
ax.scatter(x_values,y_values,s=5,c=y_values,cmap=plt.cm.Greens,
           edgecolors='none')                                             # 使用渐变色，把参数c设置成了一个y值列表，并使用参数cmap使用颜色颜色（Blues,Reds,Greens）

# 设置图表标题并给坐标轴加上标签
plt.rcParams['font.sans-serif']=['SimHei']                                # 显示中文标签
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("值的平方",fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)                                  # both表示xy轴都进行设置
# 设置每个坐标轴的取值范围
ax.axis([0,101,0,11000])

# 如果不想展示，只想保存，bbox_inches='tight'：将图表中多余的空白区域裁剪掉
plt.show()
# plt.savefig('scatter.png',bbox_inches='tight')