# -*- coding: utf-8 -*-
# 将DataFrame结果保存为Excel文件

import pandas as pd
stocks = pd.read_csv('./smallstocks.csv', parse_dates=['Date'])

format_dict = {'Date':'{:%m/%d/%y}', 'Close':'${:.2f}', 'Volume':'{:,}'}

a = (stocks.style.format(format_dict)
 .hide_index()
 .highlight_min('Close', color='red')
 .highlight_max('Close', color='green')
)

a.to_excel('min_max.xlsx')