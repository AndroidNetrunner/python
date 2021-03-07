from urllib.request import urlopen
import bs4

url1 = "https://www.mk.co.kr/news/bestclick/" #매일경제 인기뉴스
url2 = "https://www.hankyung.com/ranking" #한국경제 인기뉴스
url3 = "http://www.fnnews.com/today" #파이낸셜 뉴스 1면

html1 = urlopen(url1)
html2 = urlopen(url2)
html3 = urlopen(url3)
print("'매일경제, 한국경제, 파이낸셜뉴스', 오늘의 인기 뉴스는?\n")

bs_obj1 = bs4.BeautifulSoup(html1.read(), "html.parser") #매일경제 인기뉴스 페이지 정리해줘!

div = bs_obj1.find("div", {"class": "list_area"})        #매경 인기뉴스 경제 기사 목록만 있는 부분 div 태그 뽑기
dts = div.findAll("dt", {"class":"tit"})                 #매경 인기기사 각 헤드라인 뽑기
print("매일경제 인기 뉴스 보러가기 ->", 'https://www.mk.co.kr/news/bestclick/\n')
for mli in dts:                                           # 매경 인기뉴스 헤드라인만 모아보기
    print(mli.text)

print()
bs_obj2 = bs4.BeautifulSoup(html2.read(), "html.parser")
ul = bs_obj2.find("ul", {"class":"down_rank_news"})
divs = ul.findAll("h2")
for hli in divs:
    print(hli.text.strip())
