import pandas as pd
import datetime as dt

filename = '../同性恋数据/中国城市同性恋数据.xlsx'
savename = '中国城市同性恋数据-T.xlsx'
df = pd.read_excel(filename, index_col=0)
result = df.T
result.to_excel(savename)
