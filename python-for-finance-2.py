# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 GUO DEJIE <dejie.guo@gmail.com>
#
# Distributed under terms of the MIT license.
"""
Handling Data and Graphing - Python Programming for Finance p.2
"""
import datetime as dt

import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style

style.use('ggplot')

# start = dt.datetime(2000, 1, 1)
# end = dt.datetime(2016, 12, 31)

# df = web.DataReader('TSLA', 'yahoo', start, end)

# df.to_csv('tsla.csv')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
# print(df.head())

print(df[['Open', 'High']].head())

df['Adj Close'].plot()
plt.show()
