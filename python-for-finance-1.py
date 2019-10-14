# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 GUO DEJIE <dejie.guo@gmail.com>
#
# Distributed under terms of the MIT license.
"""
Intro and Getting Stock Price Data - Python Programming for Finance p.1
"""
import datetime as dt

import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.head())
