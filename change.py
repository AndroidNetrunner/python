from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://m.stock.nave.rcom/marketindex/index.nhn"

html = urlopen(url)
currency = html.read()
index = BeautifulSoup(currency,"html.parser")
result = index.find_all("span",{"class":"stock_price"})
name = index.find_all("strong",{"class":"stock_item"}) + index.find_all("span", {"class":"stock_item"})
exchange = {}
while True:
    for i in num:
        if inputt == "":
            break
        data_result = data_result.replace(",","")
        data_result = float(result[i].text)
        data_name = name[i].text
        exchange[data_name] = data_result
    for i in exchange:
        if inputt in i:
            print(exchange[i] * inputtt, i[-3:])
            break