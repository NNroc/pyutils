import pandas as pd
import datetime as dt
import csv


class Country:
    def __init__(self, country_name):
        self.country_name = country_name
        self.records = dict()


class Records:
    def __init__(self, date, confirmed, deaths, recovered):
        self.date = date
        self.confirmed = int(confirmed)
        self.deaths = int(deaths)
        self.recovered = recovered

    def __add__(self, other):
        self.confirmed = int(self.confirmed) + int(other.confirmed)
        self.deaths = int(self.deaths) + int(other.deaths)
        if self.recovered != '':
            # print(other, other.recovered)
            self.recovered = int(self.recovered) + int(other.recovered)
        return Records(self.date, self.confirmed, self.deaths, self.recovered)

    def __repr__(self):
        return f'<date:{self.date}, confirmed: {self.confirmed}, deaths: {self.deaths}, recovered: {self.recovered}>'


path = './csse_covid_19_daily_reports/'
save_name_confirmed = 'covid_global_confirmed.csv'
save_name_deaths = 'covid_global_deaths.csv'
save_name_recovered = 'covid_global_recovered.csv'

all_data = dict()


def add_country(global_time_series: dict, country: str, records: Records):
    if country in global_time_series:
        # print("这里是相加", country, global_time_series[country], records)
        global_time_series[country] = global_time_series[country] + records
        # print("这里是相加", country, global_time_series[country], records)
        # print()
    else:
        global_time_series[country] = records


global_time_series = dict()

# 起止日期
start_date = dt.date(2021, 1, 1)
# end_data = dt.date(2023, 1, 1)
end_data = dt.date(2023, 1, 30)
delta = dt.timedelta(days=1)
date = start_date

# 所有的日期
all_dates = []
# 所有的国家
all_country = []
while date <= end_data:
    all_dates.append(date.strftime("%Y-%m-%d"))
    date += delta

for date in all_dates:
    filename = str(date[5:7]) + '-' + str(date[8:10]) + '-' + str(date[0:4]) + '.csv'
    file = pd.read_csv(path + filename)

    with open(path + filename, 'r', encoding='GBK') as fp:
        reader = csv.DictReader(fp)
        # print(date)
        for x in reader:
            if x['Country_Region'] not in all_country:
                all_country.append(x['Country_Region'])
            add_country(global_time_series, x['Country_Region'],
                        Records(date, x['Confirmed'], x['Deaths'], x['Recovered']))
        all_data[date] = global_time_series
        global_time_series = dict()

# print(all_data)
all_country.sort()
print(all_country)

with open(save_name_confirmed, 'w', encoding='utf-8') as f:
    print(f)
    dates_str = ''
    for date in all_dates:
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country in all_country:
        # json中遍历到的日期，防止没有
        now_data = all_dates[0]
        use = ''
        for date in all_dates:
            if country not in all_data[date]:
                use = use + ',' + ''
            else:
                use = use + ',' + str(all_data[date][country].confirmed)
        f.writelines("\"" + country + "\"" + use + '\n')

with open(save_name_deaths, 'w', encoding='utf-8') as f:
    print(f)
    dates_str = ''
    for date in all_dates:
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country in all_country:
        # json中遍历到的日期，防止没有
        now_data = all_dates[0]
        use = ''
        for date in all_dates:
            if country not in all_data[date]:
                use = use + ',' + ''
            else:
                use = use + ',' + str(all_data[date][country].deaths)
        f.writelines("\"" + country + "\"" + use + '\n')

with open(save_name_recovered, 'w', encoding='utf-8') as f:
    print(f)
    dates_str = ''
    for date in all_dates:
        dates_str = dates_str + ',' + str(date)
    f.writelines('country' + dates_str + '\n')
    for country in all_country:
        # json中遍历到的日期，防止没有
        now_data = all_dates[0]
        use = ''
        for date in all_dates:
            if country not in all_data[date]:
                use = use + ',' + ''
            else:
                use = use + ',' + str(all_data[date][country].recovered)
        f.writelines("\"" + country + "\"" + use + '\n')
