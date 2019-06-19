#-*- coding: utf-8 -*-
#餐饮销量数据统计量分析
from __future__ import print_function
import pandas as pd

catering_sale = '../data/catering_sale.xls' #餐饮数据
data = pd.read_excel(catering_sale, index_col = u'日期') #读取数据，指定“日期”列为索引列
data = data[(data[u'销量'] > 400)&(data[u'销量'] < 5000)] #过滤异常数据
statistics = data.describe() #保存基本统计量

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min'] #极差,往statistics中增加range行索引，
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean'] #变异系数，往statistics中增加var行索引，
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%'] #四分位数间距，往statistics中增加dis行索引，

print(statistics)
#笔记1##################
'''
在开头加上from __future__ import print_function这句之后，即使在python2.X，使用print就得像python3.X那样加括号使用。
'''