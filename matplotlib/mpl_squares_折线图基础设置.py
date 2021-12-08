#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
'''
Pyplot 是 Matplotlib 的子库，提供了和 MATLAB 类似的绘图 API。让用户绘制 2D 图表.
subplots():可以在一张图片上绘制一个或多个图表
plot(x,y,*,):用于画图,可以绘制点和线
ax.set_title:给子图设置标题
tick_params:设置刻度标记
plt.style.use：设置子表背景
fig.autofmt_xdate():绘制倾斜的X轴坐标，避免其彼此重叠

1.绘制简单的折线图,修改标签文字和线条粗细，校正图形，使用内置样式

'''
# x,y轴的值
input_value = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

plt.style.use('ggplot')                                    # 使用内置样式，设置子表背景
fig,ax = plt.subplots()                                    # 变量fig表示整张图片，变量ax表示图片中的各个图表
ax.plot(input_value,squares,linewidth=3)

# 设置图表标题并给坐标轴加上标签
plt.rcParams['font.sans-serif']=['SimHei']                 # 显示中文标签
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("值的平方",fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)                   # both表示xy轴都进行设置
plt.show()



