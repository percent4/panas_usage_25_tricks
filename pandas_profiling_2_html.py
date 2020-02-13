# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020-02-13 21:47
import pandas as pd
import pandas_profiling

# 将pandas profiling的结果保存为HTML网页
titanic = pd.read_csv('./kaggletrain.csv')
pandas_profiling.ProfileReport(titanic).to_file('titanic.html')