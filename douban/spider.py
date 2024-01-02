import requests
import json
from bs4 import BeautifulSoup
import random
import xlsxwriter

user_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Opera/8.0 (Windows NT 5.1; U; en)',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 ',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
]


def getHeaders():
    i = random.randint(0, 10)
    user_agent = user_agents[i]
    headers = {
        'User-Agent': user_agent
    }
    return headers


def pauseComment(commenthtml):
    id = commenthtml['data-cid']
    name = commenthtml.div.a['title']
    span = commenthtml.find_all('span', attrs={"class": "short"})[0]
    text = span.text
    return id, name, text


if __name__ == '__main__':
    ids = ['']
    workbook = xlsxwriter.Workbook('data.xlsx')
    worksheet = workbook.add_worksheet('comments')

    # 写入影评数据
    rowindex = 1
    for id in ids:
        for start in range(0, 218145, 20):
            commenturl = "https://movie.douban.com/subject/4922787/comments?start=" + str(
                start) + "&limit=20&sort=new_score&status=P&percent_type="
            response2 = requests.get(commenturl, headers=getHeaders(), timeout=20)
            html = BeautifulSoup(response2.text, 'xml')
            comments = html.find_all("div", attrs={"class": "comment-item "})
            for comment in comments:
                cid, name, text = pauseComment(comment)
                worksheet.write_row(rowindex, 0, (id, cid, name, text))
                print(rowindex, id, cid, name, text)
                rowindex += 1
    workbook.close()
