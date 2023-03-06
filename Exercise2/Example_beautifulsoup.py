# Exercise2 - BeautifulSoup
import requests
from bs4 import BeautifulSoup

# main
response = requests.get("https://isin.twse.com.tw/isin/C_public.jsp?strMode=2") # 上市股票網頁
# response = requests.get("https://isin.twse.com.tw/isin/C_public.jsp?strMode=4") # 上櫃股票網頁
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select("tr td b")[0] # "股票" (上市)
# result = soup.select("tr td b")[4] # "股票" (上櫃)
while True:
    result = result.find_next("tr") # 從股票(<b>)往下找到第一個<tr>，之後就是一直往下找<tr>
    info = result.find_all("td")    # 找出<tr>裡所有的<td>
    if(info[0].text.strip() == "上市認購(售)權證"): # 用strip()把空格消掉 (上市)
    # if(info[0].text.strip() == "特別股"):   # 用strip()把空格消掉 (上櫃)
        break
    stock = []
    stock.append(info[0].text.split("　")[0])   # 股票代號 (注意是"全形"空格)
    stock.append(info[0].text.split("　")[1])   # 股票名稱 (注意是"全形"空格)
    stock.append(info[3].text)  # 市場別 
    stock.append(info[4].text)  # 產業別
    print(stock)




