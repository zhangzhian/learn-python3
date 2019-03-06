import requests
import xlwt
from bs4 import BeautifulSoup
# https://movie.douban.com/top250
# 豆瓣电影 Top 250 爬取

# 存储爬去到的数据
movie_list = []
director_list = []
time_list = []
star_list = []

for i in range(0, 10):

    link = 'https://movie.douban.com/top250?start=' + str(i*25)
    res = requests.get(link, timeout=10)
    # 该网站不需要使用headers也可以
    # res = requests.get(link, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, "lxml")
    # 寻找div class为hd的标签
    div_list = soup.find_all('div', class_='hd')
    div1_list = soup.find_all('div', class_='bd')
    div2_list = soup.find_all('div', class_='star')
    # 解析数据
    for each in div_list:
        movie = each.a.span.text.strip()
        movie_list.append(movie)

    for each in div1_list:
        info = each.p.text.strip()
        if len(info) < 3:
            continue
        time_start = info.find('20')
        if time_start < 0:
            time_start = info.find('19')
        end = info.find('...')
        gap_value = time_start - end
        time = info[end + gap_value:end + gap_value + 4]
        time_list.append(time)

        end = info.find('主')
        director = info[4:end - 3]
        director_list.append(director)

    for each in div2_list:
        info = each.text.strip()
        star = info[0:3]
        star_list.append(star)

# 保存到xls文件中
file = xlwt.Workbook()

table = file.add_sheet('sheet name')
table.write(0, 0, "排名")
table.write(0, 1, "电影")
table.write(0, 2, "时间")
table.write(0, 3, "导演")
table.write(0, 4, "评分")

for i in range(len(star_list)):
    table.write(i + 1, 0, i + 1)
    table.write(i + 1, 1, movie_list[i])
    table.write(i + 1, 2, time_list[i])
    table.write(i + 1, 3, director_list[i])
    table.write(i + 1, 4, star_list[i])

file.save('data_douban_1.xls')
