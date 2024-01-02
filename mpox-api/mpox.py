import pandas as pd
import datetime as dt
import csv


class Country:
    def __init__(self, country_name):
        self.country_name = country_name
        self.records = dict()


class Records:
    def __init__(self, date, total_cases, total_deaths, new_cases, new_deaths):
        self.date = date
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.new_cases = new_cases
        self.new_deaths = new_deaths

    def __repr__(self):
        return f'<date:{self.date}, total_cases: {self.total_cases}, total_deaths: {self.total_deaths}, ' \
               f'new_cases: {self.new_cases}, new_deaths: {self.new_deaths}>'


filename = 'owid-monkeypox-data.csv'
save_name_total_cases = 'mpox_global_total_cases.csv'
save_name_total_deaths = 'mpox_global_total_deaths.csv'
save_name_new_cases = 'mpox_global_new_cases.csv'
save_name_new_deaths = 'mpox_global_new_deaths.csv'

save_name_total_cases_week = 'mpox_global_total_cases_week.csv'
save_name_total_deaths_week = 'mpox_global_total_deaths_week.csv'
save_name_new_cases_week = 'mpox_global_new_cases_week.csv'
save_name_new_deaths_week = 'mpox_global_new_deaths_week.csv'

all_data = dict()

global_time_series = dict()

# 起止日期
start_date = dt.date(2022, 5, 1)
end_data = dt.date(2023, 1, 30)
delta = dt.timedelta(days=1)
date = start_date
# 所有的日期
all_dates = []
# 所有的国家名字
all_country_name = []
# 所有的数据
all_country = {}
while date <= end_data:
    all_dates.append(date.strftime("%Y-%m-%d"))
    date += delta

with open(filename, 'r', encoding='GBK') as fp:
    reader = csv.DictReader(fp)
    use = None
    for x in reader:
        if x['location'] not in all_country_name:
            if use is not None:
                all_country[use.country_name] = use
            all_country_name.append(x['location'])
            use = Country(x['location'])
        use.records[x['date']] = Records(x['date'],
                                         x['total_cases'], x['total_deaths'],
                                         x['new_cases'], x['new_deaths'])

if use is not None:
    all_country[use.country_name] = use
    use = None

all_country_name.sort()

with open(save_name_total_cases, 'w', encoding='utf-8') as f:
    dates_str = ''
    for date in all_dates:
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country_name in all_country_name:
        use = ''
        for date in all_dates:
            # print(country_name, ' ', date)
            if date not in all_country[country_name].records:
                use = use + ',' + ''
            else:
                use = use + ',' + str(all_country[country_name].records[date].total_cases)
        f.writelines("\"" + country_name + "\"" + use + '\n')

with open(save_name_total_deaths, 'w', encoding='utf-8') as f:
    dates_str = ''
    for date in all_dates:
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country_name in all_country_name:
        use = ''
        for date in all_dates:
            # print(country_name, ' ', date)
            if date not in all_country[country_name].records:
                use = use + ',' + ''
            else:
                use = use + ',' + str(all_country[country_name].records[date].total_deaths)
        f.writelines("\"" + country_name + "\"" + use + '\n')

with open(save_name_new_cases, 'w', encoding='utf-8') as f:
    dates_str = ''
    for date in all_dates:
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country_name in all_country_name:
        use = ''
        for date in all_dates:
            # print(country_name, ' ', date)
            if date not in all_country[country_name].records:
                use = use + ',' + ''
            else:
                use = use + ',' + str(all_country[country_name].records[date].new_cases)
        f.writelines("\"" + country_name + "\"" + use + '\n')

with open(save_name_new_deaths, 'w', encoding='utf-8') as f:
    dates_str = ''
    for date in all_dates:
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country_name in all_country_name:
        use = ''
        for date in all_dates:
            # print(country_name, ' ', date)
            if date not in all_country[country_name].records:
                use = use + ',' + ''
            else:
                use = use + ',' + str(all_country[country_name].records[date].new_deaths)
        f.writelines("\"" + country_name + "\"" + use + '\n')

print('初始生成完成')

# 生成每周数据
# 累计
with open(save_name_total_cases_week, 'w', encoding='utf-8') as f:
    dates_str = ''
    day1 = 1
    for date in all_dates:
        if day1 != 7:
            day1 += 1
            continue
        day1 = 1
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country_name in all_country_name:
        use = ''
        num = 1
        for date in all_dates:
            if num != 7:
                num += 1
                continue
            num = 1
            # print(country_name, ' ', date)
            if date not in all_country[country_name].records:
                use = use + ',' + ''
            else:
                use = use + ',' + str(all_country[country_name].records[date].total_cases)
        f.writelines("\"" + country_name + "\"" + use + '\n')

with open(save_name_total_deaths_week, 'w', encoding='utf-8') as f:
    dates_str = ''
    day1 = 1
    for date in all_dates:
        if day1 != 7:
            day1 += 1
            continue
        day1 = 1
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country_name in all_country_name:
        use = ''
        num = 1
        for date in all_dates:
            if num != 7:
                num += 1
                continue
            num = 1
            # print(country_name, ' ', date)
            if date not in all_country[country_name].records:
                use = use + ',' + ''
            else:
                use = use + ',' + str(all_country[country_name].records[date].total_deaths)
        f.writelines("\"" + country_name + "\"" + use + '\n')

# 新增
with open(save_name_new_cases_week, 'w', encoding='utf-8') as f:
    dates_str = ''
    day1 = 1
    for date in all_dates:
        if day1 != 7:
            day1 += 1
            continue
        day1 = 1
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country_name in all_country_name:
        use = ''
        num = 1
        flag = 0
        sum = 0
        for date in all_dates:
            if date in all_country[country_name].records:
                sum = sum + int(float(all_country[country_name].records[date].new_cases))
                flag = 1
            if num != 7:
                num += 1
                continue
            # print(country_name, ' ', date)
            if flag == 0:
                use = use + ',' + ''
            else:
                use = use + ',' + str(sum)
            num = 1
            sum = 0
            flag = 0
        f.writelines("\"" + country_name + "\"" + use + '\n')

with open(save_name_new_deaths_week, 'w', encoding='utf-8') as f:
    dates_str = ''
    day1 = 1
    for date in all_dates:
        if day1 != 7:
            day1 += 1
            continue
        day1 = 1
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country_name in all_country_name:
        use = ''
        num = 1
        flag = 0
        sum = 0
        for date in all_dates:
            if date in all_country[country_name].records:
                sum = sum + int(float(all_country[country_name].records[date].new_deaths))
                flag = 1
            if num != 7:
                num += 1
                continue
            # print(country_name, ' ', date)
            if flag == 0:
                use = use + ',' + ''
            else:
                use = use + ',' + str(sum)
            num = 1
            sum = 0
            flag = 0
        f.writelines("\"" + country_name + "\"" + use + '\n')

# 转置
df = pd.read_csv(save_name_total_cases, index_col=0)
result = df.T
result.to_csv(save_name_total_cases)
df = pd.read_csv(save_name_total_deaths, index_col=0)
result = df.T
result.to_csv(save_name_total_deaths)
df = pd.read_csv(save_name_new_deaths, index_col=0)
result = df.T
result.to_csv(save_name_new_deaths)
df = pd.read_csv(save_name_new_cases, index_col=0)
result = df.T
result.to_csv(save_name_new_cases)

df = pd.read_csv(save_name_total_cases_week, index_col=0)
result = df.T
result.to_csv(save_name_total_cases_week)
df = pd.read_csv(save_name_total_deaths_week, index_col=0)
result = df.T
result.to_csv(save_name_total_deaths_week)
df = pd.read_csv(save_name_new_deaths_week, index_col=0)
result = df.T
result.to_csv(save_name_new_deaths_week)
df = pd.read_csv(save_name_new_cases_week, index_col=0)
result = df.T
result.to_csv(save_name_new_cases_week)
print('转置操作完成')
