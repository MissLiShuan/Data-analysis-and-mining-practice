#-*- coding: utf-8 -*-
#菜品盈利数据 帕累托图
from __future__ import print_function
import pandas as pd

#初始化参数
dish_profit = '../data/catering_dish_profit.xls' #餐饮菜品盈利数据
data = pd.read_excel(dish_profit, index_col = u'菜品名')
data = data[u'盈利'].copy()
[data.values].sort(reverse = True)#.sort是列表的排序函数，reverse = True表示降序

import matplotlib.pyplot as plt #导入图像库
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

plt.figure()
data.plot(kind='bar')#绘制条形图
plt.ylabel(u'盈利（元）')
p = 1.0*data.cumsum()/data.sum()#累计求和/总和
p.plot(color = 'r', secondary_y = True, style = '-o',linewidth = 2)#指定secondary_y为True，只是将右轴作为索引
plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) #添加注释，即85%处的标记。这里包括了指定箭头样式。
plt.ylabel(u'盈利（比例）')
plt.show()
#笔记1################### cumsums和cumprod函数###################################
'''

>>>a = np.array([1,2,3],[4,5,6]])
 >>>a
 array([[1,2,3],
        [4,5,6]])
 >>>a.cumsum(0)
 array([[1,2,3],
        [5,7,9]])
 >>>a.cumprod(1)
 array([[1,2,6],
        [4,20,120]])

这两个函数中难点就是其中参数0,1
其中0代表列的计算，1代表行的计算，即对列和行分别累积求和、 积。
而且其结果不聚合，产生的是中间数组

'''