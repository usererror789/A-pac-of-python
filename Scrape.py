"""
HTTP ：Hypertext Transfer Protocol 超文本传输协议，用于客户端与网站进行传输的响应协议
分为两类：get方法和post方法，前者用于获取，后者用于传输文本，比如账号密码
HTTP请求格式：请求行，请求头，请求体

请求行
POST /user/info?new_user=true HTTP/1.1
方法类型 /资源路径?查询参数 协议版本

请求头
Host:www.example.com
User-Agent:curl/7.77.0  (发送请求的客户端地址）
Accept:*/*  (接收HTML:text/html  接收JSON:application/json  接收多种数据类型:text/html,application/json  接收全部:*/*)

请求体
{"username":"64494",
"password":"123456"}
通常用于POST方法，GET请求体为空


HTTP响应格式：状态行，响应头，响应体

状态行
HTTP/1.1 200 OK
协议版本 状态码 状态消息

响应头
Date:Fri,27 Jan 2023 02:10:48 GMT
Content-Type:text/html;charset=utf-8

响应体
<!DOCTYPE html>
"""

'''
import requests
from bs4 import BeautifulSoup

#更改发送请求的代理
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64"}

#传入网页URL
response = requests.get("http://books.toscrape.com/", headers=headers)

#获取响应状态码
print(response)
print(response.status_code)
if response.ok:
    print(response.text)
else:
    print('请求失败')

#解析HTML
content = response.text
soup = BeautifulSoup(content, "html.parser")

all_prices = soup.find_all('p', attrs={"class": "price_color"})
price_list = []
for price in all_prices:
    price_list.append(price.string[2:])
print(price_list)

all_titles = soup.find_all('h3')
title_list = []
for title in all_titles:
    all_links = title.find_all('a')
    for link in all_links:
        title_list.append(link.string)
print(title_list)
'''

#爬虫实战


'''
top250_list = []

for start_num in range(0, 250, 25):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"}
    content = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers).text
    soup = BeautifulSoup(content, "html.parser")
    all_span = soup.findAll("span", attrs={"class": "title"})

    for span in all_span:
        if span.string[1] != '/':
            top250_list.append(span.string)
print(top250_list)
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
content = requests.get("http://www.nmc.cn/publish/forecast/AAH/wuhu.html", headers=headers).content

soup = BeautifulSoup(content, "lxml")


seven_date = soup.find_all("div", attrs={"class": "date"})
seven_weather_daily = soup.find_all("div", attrs={"class": "desc"})[0:13:2]
seven_weather_night = soup.find_all("div", attrs={"class": "desc"})[1:14:2]
seven_wind_d_daily = soup.find_all("div", attrs={"class": "windd"})[0:13:2]
seven_wind_d_night = soup.find_all("div", attrs={"class": "windd"})[1:14:2]
seven_wind_daily = soup.find_all("div", attrs={"class": "winds"})[0:13:2]
seven_wind_night = soup.find_all("div", attrs={"class": "winds"})[1:14:2]

lt = []
for i in seven_wind_daily:
    lt += i.find_next_siblings('div', limit=2)
seven_temperature_max = lt[0:13:2]
seven_temperature_min = lt[1:14:2]

weather = pd.DataFrame({
    "日期": [date.text for date in seven_date],
    "日间天气": [wea.text for wea in seven_weather_daily],
    "夜间天气": [wea.text for wea in seven_weather_night],
    "日间风速": [win.text for win in seven_wind_daily],
    "夜间风速": [win.text for win in seven_wind_night],
    "日间风向": [win.text for win in seven_wind_d_daily],
    "夜间风向": [win.text for win in seven_wind_d_night],
    "最高温度": [temp.text for temp in seven_temperature_max],
    "最低温度": [temp.text for temp in seven_temperature_min]
})

weather.to_csv("D:\PyScrape\WuHu_seven_days_weather.csv",index=False)