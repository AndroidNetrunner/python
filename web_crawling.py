from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.boardgamegeek.com/xmlapi/boardgame/1"
webpage = urlopen(url).read()
index = BeautifulSoup(webpage,"html.parser")
print(index)