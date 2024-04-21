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

# filename = './savedrecs.xls'
# df = pd.read_excel(filename, dtype=str)
# a = df['Authors']
# author2article_num = {}
# for aa in a:
#     authors = aa.split("; ")
#     for author in authors:
#         if author not in author2article_num:
#             author2article_num[author] = 1
#         else:
#             author2article_num[author] += 1
# sorted_list = sorted(author2article_num.items(), key=lambda item: item[1], reverse=True)
# print(sorted_list[0:5])


filename = './virus_num.xlsx'
df = pd.read_excel(filename)
virusss = df.values.tolist()
m = {}
m['ebola'] = 0
m['marburg'] = 0
m['pestis'] = 0
m['botulinum'] = 0
m['anthra'] = 0
m['lassa'] = 0
m['Rift Valley fever virus'] = 0
m['Venezuelan Equine Encephalitis Virus'] = 0
with open(filename, 'r') as file:
    virus_num = {}
    for v in virusss:
        if "埃博拉" in v[1] or 'ebo' in v[0].lower():
            m['ebola'] += v[2]
            continue
        elif "马尔堡" in v[1] or 'marburg' in v[0].lower() or 'marv' in v[0].lower():
            m['marburg'] += v[2]
            continue
        elif "鼠疫" in v[1] or 'pestis' in v[0].lower():
            m['pestis'] += v[2]
            continue
        elif "肉毒" in v[1] or 'botulinum' in v[0].lower():
            m['botulinum'] += v[2]
            continue
        elif "炭疽" in v[1] or 'anthra' in v[0].lower():
            m['anthra'] += v[2]
            continue
        elif "拉萨" in v[1] or 'lassa' in v[0].lower():
            m['lassa'] += v[2]
            continue
        elif "裂谷热" in v[1] or 'RVFV' in v[0] or 'rift' in v[0].lower():
            m['Rift Valley fever virus'] += v[2]
            continue
        elif "马脑炎" in v[1] or 'venezuelan' in v[0].lower() or 'VEEV' in v[0]:
            m['Venezuelan Equine Encephalitis Virus'] += v[2]
            continue
        else:
            m[v[0]] = v[2]
sorted_list = sorted(m.items(), key=lambda item: item[1], reverse=True)
print(sorted_list[0:20])
