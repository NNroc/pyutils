import pandas as pd

# filename = './(无水印)机构同义词.xlsx'
# df = pd.read_excel(filename)
# a = df['USAMRIID']
# stri = "\""
# for aa in a:
#     stri = stri + str(aa) + "\" OR \""
# print(stri)

# filename = './savedrecs.xls'
# df = pd.read_excel(filename)
# a = df['USAMRIID']
# stri = "\""
# for aa in a:
#     stri = stri + str(aa) + "\" OR \""
# print(stri)

# filename = './savedrecs.xls'
# df = pd.read_excel(filename, dtype=str)
# a = df['Indexed Date']
# year_list = [0 for i in range(30)]
# for aa in a:
#     year = str(aa[0:4])
#     print()
#     year_int = int(year) - 2000
#     year_list[year_int] += 1
# print(year_list)
# print(sum(year_list))
# print(1897 / 23)

filename = './savedrecs.xls'
df = pd.read_excel(filename, dtype=str)
a = df['Authors']
author2article_num = {}
for aa in a:
    authors = aa.split("; ")
    for author in authors:
        if author not in author2article_num:
            author2article_num[author] = 1
        else:
            author2article_num[author] += 1
sorted_list = sorted(author2article_num.items(), key=lambda item: item[1], reverse=True)
print(sorted_list[0:5])
