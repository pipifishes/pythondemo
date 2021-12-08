import  requests
from plotly.graph_objs import Bar, Layout
from plotly.offline import offline

'''
https://api.github.com/search/repositories?q=language:python&sort=stars

plotly:来生成交互式表格（可以用鼠标拖动大小的），plotly不能直接接受函数range()的结果，需要转成列表
plotly：允许在文本元素中使用html
类Bar():表示用于绘制条形图的数据集，需要一个存储x值的列表和一个存储y值的列表
类Layout():返回一个指定图表布局和配置的对象
offline.plot():这个函数需要一个包含数据和布局对象的字典，还接受一个文件名
键'hovertext'：提取列表文本，并在观察者鼠标指向条形时显示

1.爬虫爬githup API返回json格式，处理响应字典，
2.遍历所有仓库，创建交互式条形图，给条形指定颜色和边框
3.添加自定义工具提示
4.不再用repo_name作为x轴，用带有url链接的repo_links作为x轴
'''
# 用F12拿到的请求头，主要是为了伪装成浏览器绕过反爬措施
f12_headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
url ="https://api.github.com/search/repositories?q=language:python&sort=stars"
# 返回一个response对象，这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等
response = requests.get(url, headers = f12_headers, verify=False)
# print(response.text)
# 打印status_code,核实调用是否成功
print("status_code:",response.status_code)
# 将API响应赋值给一个变量
response_dict = response.json()
# 处理结果，返回keys
print(response_dict.keys())

# 探索有关仓库的信息，打印’items‘有多少个
items = response_dict['items']
print("items number:",len(items))

# 整理星数做y轴
stars = [item['stargazers_count'] for item in items]
# 整理url链接做x轴
repo_links = []
for item in items:
    repo_name = item['name']
    repo_url = item['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"  #创建一个指向项目的链接，HTML标记a格式：<a href="url"> 链接文本 </a>
    repo_links.append(repo_link)
# 创建给各个项目显示的文本
labels = []
for item in items:
    owner = item['owner']['login']
    description = item['description']
    label = f"{owner}<br />{description}"   #<br />：html的换行符
    labels.append(label)


# 可视化,绘制直方图
data = [{
    'type':'bar',
    'x':repo_links,
    'y':stars,

    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,

    'hovertext':labels,
}]
my_layout = {
    'title':'github上最受欢迎的python项目',
    'xaxis':{'title':'仓库名'},
    'yaxis':{'title':'星数'},
}
# 生成图表
fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_url_repos.html')