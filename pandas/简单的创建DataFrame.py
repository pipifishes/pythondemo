import pandas as pd
'''
1. Series:是由一组数据与一组索引（行索引）组成的数据结构
2. pd.DataFrame用法：
   DataFrame是由一组数据与一对索引（行索引和列索引）组成的表格型数据结构
   其中第一个参数是存放在DataFrame里的数据，第二个参数index就是之前说的行名，第三个参数columns是之前说的列名
'''
# 创建一个DataFrame
data = [
    ['Ohio2','Ohio2','Ohio2','Nevada2','Nevada2'],
    [2002,2012,2022,2012,2022],
    [1.52,1.72,3.62,2.42,2.92],]
# 设置第二三个参数，指定行，列索引
df = pd.DataFrame(data,index = ['state','year','pop'],columns= ['A','B','C','D','E'])
print(df)

# 获取DataFrame的行列索引
print(df.index)
print(df.columns)