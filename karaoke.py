from urllib.request import urlopen
import bs4

url= "http://m.keumyoung.kr/songsearch/search_more.asp?s_cd=1&s_value="

number = input("검색하실 노래방 노래의 번호를 입력해주세요: ")
url += number
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(),"html.parser")

song_name = bs_obj.select_one('div.table1 > table > tbody > tr > td > a')
singer = bs_obj.select_one("span.artist")
if song_name and singer:
    print(song_name.text, "-", singer.text.strip())
else:
    print("등록되지 않은 번호입니다.")