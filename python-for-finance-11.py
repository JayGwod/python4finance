# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 GUO DEJIE <dejie.guo@gmail.com>
#
# Distributed under terms of the MIT license.
"""
Creating labels for Machine Learning - Python Programming for Finance p. 11
"""
import pickle
from collections import Counter

import numpy as np
import pandas as pd


def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days + 1):
        df['{}_{}d'.format(
            ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)

    return tickers, df


def buy_sell_hold(*args):
    cols = [c for c in args]
    requirment = 0.02

    for col in cols:
        if col > requirment:
            return 1

        if col < -requirment:
            return -1

    return 0


def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list(
        map(buy_sell_hold, df['{}_1d'.format(ticker, i)],
            df['{}_2d'.format(ticker, i)], df['{}_3d'.format(ticker, i)],
            df['{}_4d'.format(ticker, i)], df['{}_5d'.format(ticker, i)],
            df['{}_6d'.format(ticker, i)], df['{}_7d'.format(ticker, i)]))

    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:', Counter(str_vals))
    df.fillna(0, inplace=True)
