from urllib.request import urlopen
import bs4
import datetime

today = str(datetime.date.today()).replace("-","")
# url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&listType=title&date=" + today
url = "https://www.daishin.com/content/w/invest/news/news.ds?p=2062&v=1442&m=1073"
html = urlopen(url)
print(html.read())
