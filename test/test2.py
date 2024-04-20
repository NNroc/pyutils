import pandas as pd

filename = '../同性恋数据/中国城市同性恋数据.xlsx'
df = pd.read_excel(filename, index_col=0)
