from lxml import html

import requests


# 获取网页中的数据（网页源代码）
def get_urls(url):
    # 反爬 模拟浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 6.1; win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/72.0.3626.121 Safari/537.36'

    }
    response = requests.get(url, headers)
    return response.text


# 获取网页图片链接（爬取的那个漫画图片）
def html_result(text):
    html1 = html.etree.HTML(text)
    # print(html)
    # // 可以提取某个标签的所有的信息
    # @选取属性
    # / 选择一个标签
    img_urls = html1.xpath('//div[@class="main-content"]//img/@src')
    return img_urls


# 下载网页当中的数据
def get_img(url, name):
    response = requests.get(url)
    with open('G:\\need\\py\\test\%s.jpg' % name, 'wb') as f:
        f.write(response.content)


# 定义一个函数来调用者三个功能
def main():
    url = 'https://www.manhuadao.cn/Comic/ComicView?comicid=58ddafd127a7c1392c230b8e&chapterid=2348841'
    result = get_urls(url)
    image_urls = html_result(result)
    for u in image_urls:
        image_name = u.split('/')[-1]
        image_name2 = image_name.split('.')[0]
        image_name3 = image_name2.split('-')[-1]
        get_img(u, image_name3)
        print(image_name3)


# 执行程序
if __name__ == '__main__':
    main()
