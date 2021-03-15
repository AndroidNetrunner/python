from urllib.request import urlopen
import bs4

url1 = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=101"
html = urlopen(url1)
# print(html.read())
