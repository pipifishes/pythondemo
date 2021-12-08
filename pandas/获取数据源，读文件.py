#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
'''
1. Series:是由一组数据与一组索引（行索引）组成的数据结构
2. pd.DataFrame用法：
   DataFrame是由一组数据与一对索引（行索引和列索引）组成的表格型数据结构
   其中第一个参数是存放在DataFrame里的数据，第二个参数index就是之前说的行名，第三个参数columns是之前说的列名
3. 指定行索引（index_col：默认是使用源数据表的第一列作为行索引）;指定列索引（header: 默认是使用源数据表的第一行作为列索引）
4. csv默认文件中的数据都是以逗号分开的
'''

# 读取xlsx文件,选取表格；指定行索引或者列索引；如果我们只想提取前3列，通过usecols参数来提取指定列
df1 = pd.read_excel(r"C:\Users\ext.huaxiang.zhu\PycharmProjects\pythondemo\pandas\test.xlsx",sheet_name="表1")
print(df1)
df1_1 = pd.read_excel(r"C:\Users\ext.huaxiang.zhu\PycharmProjects\pythondemo\pandas\test.xlsx",sheet_name="表1",index_col=2)
df1_2 = pd.read_excel(r"C:\Users\ext.huaxiang.zhu\PycharmProjects\pythondemo\pandas\test.xlsx",sheet_name="表1",usecols=[0,3])
print(df1_2)

# 读取csv文件;指明分隔符号;指明读取行数
df2 = pd.read_csv(r"C:\Users\ext.huaxiang.zhu\PycharmProjects\pythondemo\pandas\表格\death_valley.csv")
print(df2)
df2_1 = pd.read_csv(r"C:\Users\ext.huaxiang.zhu\PycharmProjects\pythondemo\pandas\表格\death_valley.csv",sep=" ")
df2_2 = pd.read_csv(r"C:\Users\ext.huaxiang.zhu\PycharmProjects\pythondemo\pandas\表格\death_valley.csv",nrows=4)
print(df2_2)

# 读取txt文件；要看文件分隔方式
df3 = pd.read_table(r"C:\Users\ext.huaxiang.zhu\PycharmProjects\pythondemo\pandas\test.txt",sep="\t",encoding="gbk")
print(df3)

# 读取sql文件;只想展示前4行;shape获取数据表的行列数；利用info获取数据类型
conn = pymysql.connect(host='rm-uf633mxv6kkfa182tdo.mysql.rds.aliyuncs.com', port=3306, user='uaes_admin', passwd='Handhand1', charset='utf8')
conn.select_db('test3')
sql = "select * from user;"
df4 = pd.read_sql(sql,conn)
print(df4)
print(df4.head(4))
print(df4.shape)   # shape是不包括行列索引的