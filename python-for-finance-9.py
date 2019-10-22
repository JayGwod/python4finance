# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 GUO DEJIE <dejie.guo@gmail.com>
#
# Distributed under terms of the MIT license.
"""
Preprocessing data for Machine Learning - Python Programming for Finance p. 9
"""
import datetime as dt
import os
import pickle

import bs4 as bs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import requests
from matplotlib import style

style.use('ggplot')
