from plotly.graph_objs import Bar, Layout
from plotly.offline import offline

from dice import Dice
'''
plotly:来生成交互式表格（可以用鼠标拖动大小的），plotly不能直接接受函数range()的结果，需要转成列表
类Bar():表示用于绘制条形图的数据集，需要一个存储x值的列表和一个存储y值的列表
类Layout():返回一个指定图表布局和配置的对象
offline.plot():这个函数需要一个包含数据和布局对象的字典，还接受一个文件名

先获取100次投掷一次骰子出现的点数，统计出现各个点数出现次数，直方图展示
'''
# 创建一个Dice实例
d = Dice()

# 统计骰子出现的点数
results = []
for i in range(100):
     result = d.roll_dice()
     results.append(result)
# print(results)

# 统计出现各个点数出现次数
statistics = []
for value in range(1,d.num_sides+1):
     res = results.count(value)
     statistics.append(res)
print(statistics)

# 直方图展示
x_value = list(range(1,d.num_sides+1))
data = [Bar(x=x_value,y=statistics)]
# 配置坐标轴，每个配置选项都是一个字典
x_axis_config = {'title':'结果'}
y_axis_config = {'title':'结果的频率'}
# 设置表格名称，并传入x,y轴的配置字典
my_layout = Layout(title='投掷100次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
# 生成图表
offline.plot({'data':data,'layout':my_layout},filename='dice.html')



