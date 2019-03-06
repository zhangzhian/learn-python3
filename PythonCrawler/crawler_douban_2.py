import requests
import xlwt
from bs4 import BeautifulSoup
# https://movie.douban.com/top250
# 豆瓣电影排行榜
# 豆瓣新片榜 · · · · · ·

# 存储爬去到的数据
movie_list = []
director_list = []
time_list = []
star_list = []


link = 'https://movie.douban.com/chart'
res = requests.get(link, timeout=10)
# 该网站不需要使用headers也可以
# res = requests.get(link, headers=headers, timeout=10)
soup = BeautifulSoup(res.text, "lxml")
# 寻找div class为hd的标签
div1_list = soup.find_all('div', class_='pl2')
div2_list = soup.find_all('div', class_='star clearfix')
# 解析数据
for each in div1_list:
    movie = each.a.text.strip()
    movie_split = movie.split("/")
    movie_list.append(movie_split[0].strip())
    info = each.p.text.strip()
    splitStr = info.split("/")
    movie_time = ""
    movie_name = ""
    for str in splitStr:
        str_deal = str.strip()
        if str_deal.startswith("19") or str_deal.startswith("20"):
            if movie_time == "":
                movie_time = str
        else:
            if movie_name == "":
                movie_name = str
            else:
                break
    time_list.append(movie_time)
    director_list.append(movie_name)

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
table.write(0, 3, "第一主演")
table.write(0, 4, "评分")

for i in range(len(star_list)):
    table.write(i + 1, 0, i + 1)
    table.write(i + 1, 1, movie_list[i])
    table.write(i + 1, 2, time_list[i])
    table.write(i + 1, 3, director_list[i])
    table.write(i + 1, 4, star_list[i])

file.save('data_douban_2.xls')
