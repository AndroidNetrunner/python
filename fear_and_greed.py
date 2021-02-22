from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://money.cnn.com/data/fear-and-greed/")

data = BeautifulSoup(url, "html.parser")
div = data.find("div", {"id":"needleChart"})
li = div.find_all("li")
numbers = []

texts = ["오늘의 수치" ,"장 마감 수치", "1주 전 수치", "1달 전 수치", "1년 전 수치"]
for i in li:
    text = i.text.split()
    numbers.append((int(text[-2]),text[-1]))
for i in range(len(texts)):
    print(texts[i] + ":", numbers[i][0], numbers[i][1])

# ul.li[0]
# <div class="modContent feargreed">
# <div id="needleChart" style="background-image:url(&#39;http://markets.money.cnn.com/Marketsdata/uploadhandler/z718f7d0az4912895edf43423a807b6255351d1ba7.png&#39;);">
# <ul>
# <li>
# Fear &amp; Greed Now: 72 (Greed)</li>
# <li>
# Fear &amp; Greed Previous Close: 65 (Greed)</li>
# <li>
# Fear &amp; Greed 1 Week Ago: 67 (Greed)</li>
# <li>
# Fear &amp; Greed 1 Month Ago: 59 (Greed)</li>
# <li>
# Fear &amp; Greed 1 Year Ago: 74 (Greed)</li>
# </ul>
# </div>
# <div id="needleAsOfDate">
# Last updated Jan 21 at 5:02pm</div>
# <div class="indicatorHeading">
# <h3>
# Seven Fear &amp; Greed Indicators</h3>
# How we calculate the index <a href="//money.cnn.com/investing/about-fear-greed-tool/index.html ">
# More &raquo;</a>
# </div>
# <div class="indicatorContainer">
# <div class="panel extremegreed">
# <div class="label clearfix">
# <div class="wsod_fLeft">
# <span class="arrow open">
# </span>
# Market Momentum</div>
# <div class="wsod_fRight">
# Extreme Greed</div>
# </div>
# <div class="detail clearfix">
# <div class="wsod_fLeft smarttext">
# <p>
# The S&P 500 is 9.93% above its 125-day average. This is further above the average than has been typical during the last two years and rapid increases like this often indicate extreme greed.</p>
# <p>
# Last changed Jan 15 from a <span class='greed'>
# Greed</span>
#  rating</p>
# <p class="asof">
# Updated Jan 21 at 5:02pm</p>
# </div>
# <div class="wsod_fRight wsod_fgIndicatorCht" style="padding-left:0; float:right; background-position:0 -0px;background-image:url(&#39;http://markets.money.cnn.com/Marketsdata/Api/Chart/FearGreedHistoricalImage?inputOrder=SPXPtile,NHNLPtile,McOscPtile,StkBdPtile,VIXPtile,PutCallPtile,IGHYPtile,AvgPtileModel&#39;);">
# &nbsp;</div>
# <div class="clearFloat">
# </div>
# </div>
# </div>
# <div class="panel extremegreed">
# <div class="label clearfix">
# <div class="wsod_fLeft">
# <span class="arrow">
# </span>
# Stock Price Strength</div>
# <div class="wsod_fRight">
# Extreme Greed</div>
# </div>
# <div class="detail clearfix hide">
# <div class="wsod_fLeft smarttext">
# <p>
# The number of stocks hitting 52-week highs exceeds the number hitting lows and is at the upper end of its range, indicating extreme greed.</p>
# <p>
# Last changed Nov 23 from a <span class='greed'>
# Greed</span>
#  rating</p>
# <p class="asof">
# Updated Jan 21 at 4:00pm</p>
# </div>
# <div class="wsod_fRight wsod_fgIndicatorCht" style="padding-left:0; float:right; background-position:0 -164px;background-image:url(&#39;http://markets.money.cnn.com/Marketsdata/Api/Chart/FearGreedHistoricalImage?inputOrder=SPXPtile,NHNLPtile,McOscPtile,StkBdPtile,VIXPtile,PutCallPtile,IGHYPtile,AvgPtileModel&#39;);">
# &nbsp;</div>
# <div class="clearFloat">
# </div>
# </div>
# </div>
# <div class="panel greed">
# <div class="label clearfix">
# <div class="wsod_fLeft">
# <span class="arrow">
# </span>
# Stock Price Breadth</div>
# <div class="wsod_fRight">
# Greed</div>
# </div>
# <div class="detail clearfix hide">
# <div class="wsod_fLeft smarttext">
# <p>
# The McClellan Volume Summation Index measures advancing and declining volume on the NYSE. During the last month, approximately 7.08% more of each day's volume has traded in advancing issues than in declining issues, pushing this indicator towards the upper end of its range for the last two years.</p>
# <p>
# Last changed Jan 20 from an <span class='extremegreed'>
# Extreme Greed</span>
#  rating</p>
# <p class="asof">
# Updated Jan 21 at 4:00pm</p>
# </div>
# <div class="wsod_fRight wsod_fgIndicatorCht" style="padding-left:0; float:right; background-position:0 -328px;background-image:url(&#39;http://markets.money.cnn.com/Marketsdata/Api/Chart/FearGreedHistoricalImage?inputOrder=SPXPtile,NHNLPtile,McOscPtile,StkBdPtile,VIXPtile,PutCallPtile,IGHYPtile,AvgPtileModel&#39;);">
# &nbsp;</div>
# <div class="clearFloat">
# </div>
# </div>
# </div>
# <div class="panel greed">
# <div class="label clearfix">
# <div class="wsod_fLeft">
# <span class="arrow">
# </span>
# Safe Haven Demand</div>
# <div class="wsod_fRight">
# Greed</div>
# </div>
# <div class="detail clearfix hide">
# <div class="wsod_fLeft smarttext">
# <p>
# Stocks have outperformed bonds by 5.50 percentage points during the last 20 trading days. This is close to the strongest performance for stocks relative to bonds in the past two years and indicates investors are rotating into stocks from the relative safety of bonds.</p>
# <p>
# Last changed Jan 20 from a <span class='neutral'>
# Neutral</span>
#  rating</p>
# <p class="asof">
# Updated Jan 20 at 7:00pm</p>
# </div>
# <div class="wsod_fRight wsod_fgIndicatorCht" style="padding-left:0; float:right; background-position:0 -492px;background-image:url(&#39;http://markets.money.cnn.com/Marketsdata/Api/Chart/FearGreedHistoricalImage?inputOrder=SPXPtile,NHNLPtile,McOscPtile,StkBdPtile,VIXPtile,PutCallPtile,IGHYPtile,AvgPtileModel&#39;);">
# &nbsp;</div>
# <div class="clearFloat">
# </div>
# </div>
# </div>
# <div class="panel neutral">
# <div class="label clearfix">
# <div class="wsod_fLeft">
# <span class="arrow">
# </span>
# Market Volatility</div>
# <div class="wsod_fRight">
# Neutral</div>
# </div>
# <div class="detail clearfix hide">
# <div class="wsod_fLeft smarttext">
# <p>
# The CBOE Volatility Index (VIX) is at 21.32. This is a neutral reading and indicates that market risks appear low.</p>
# <p>
# Last changed Nov 3 from an <span class='extremefear'>
# Extreme Fear</span>
#  rating</p>
# <p class="asof">
# Updated Jan 21 at 4:14pm</p>
# </div>
# <div class="wsod_fRight wsod_fgIndicatorCht" style="padding-left:0; float:right; background-position:0 -656px;background-image:url(&#39;http://markets.money.cnn.com/Marketsdata/Api/Chart/FearGreedHistoricalImage?inputOrder=SPXPtile,NHNLPtile,McOscPtile,StkBdPtile,VIXPtile,PutCallPtile,IGHYPtile,AvgPtileModel&#39;);">
# &nbsp;</div>
# <div class="clearFloat">
# </div>
# </div>
# </div>
# <div class="panel fear">
# <div class="label clearfix">
# <div class="wsod_fLeft">
# <span class="arrow">
# </span>
# Put and Call Options</div>
# <div class="wsod_fRight">
# Fear</div>
# </div>
# <div class="detail clearfix hide">
# <div class="wsod_fLeft smarttext">
# <p>
# SmartText not available.</p>
# <p>
# Last changed Jan 14 from an <span class='extremegreed'>
# Extreme Greed</span>
#  rating</p>
# <p class="asof">
# Updated Jan 14 at 7:00pm</p>
# </div>
# <div class="wsod_fRight wsod_fgIndicatorCht" style="padding-left:0; float:right; background-position:0 -820px;background-image:url(&#39;http://markets.money.cnn.com/Marketsdata/Api/Chart/FearGreedHistoricalImage?inputOrder=SPXPtile,NHNLPtile,McOscPtile,StkBdPtile,VIXPtile,PutCallPtile,IGHYPtile,AvgPtileModel&#39;);">
# &nbsp;</div>
# <div class="clearFloat">
# </div>
# </div>
# </div>
# <div class="panel fear last">
# <div class="label clearfix">
# <div class="wsod_fLeft">
# <span class="arrow">
# </span>
# Junk Bond Demand</div>
# <div class="wsod_fRight">
# Fear</div>
# </div>
# <div class="detail clearfix hide">
# <div class="wsod_fLeft smarttext">
# <p>
# Investors in low quality junk bonds are accepting 2.17 percentage points in additional yield over safer investment grade corporate bonds. While this spread is historically low, it is elevated compared to recent levels and suggests that investors are becoming more risk averse.</p>
# <p>
# Last changed Jan 15 from an <span class='extremefear'>
# Extreme Fear</span>
#  rating</p>
# <p class="asof">
# Updated Jan 20 at 7:00pm</p>
# </div>
# <div class="wsod_fRight wsod_fgIndicatorCht" style="padding-left:0; float:right; background-position:0 -984px;background-image:url(&#39;http://markets.money.cnn.com/Marketsdata/Api/Chart/FearGreedHistoricalImage?inputOrder=SPXPtile,NHNLPtile,McOscPtile,StkBdPtile,VIXPtile,PutCallPtile,IGHYPtile,AvgPtileModel&#39;);">
# &nbsp;</div>
# <div class="clearFloat">
# </div>
# </div>
# </div>
# </div>
# <h3>
# Fear &amp; Greed Over Time</h3>
# <div id="feargreedOverTime" style="background-image:url(&#39;http://markets.money.cnn.com/Marketsdata/Api/Chart/FearGreedHistoricalImage?chartType=AvgPtileModel&#39;);">
# &nbsp;</div>
# </div>


