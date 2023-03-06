# Exercise3 - Load JSON
import requests
import json
from fake_useragent import UserAgent

# main
ua = UserAgent()
# 2330 即時股價
url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_2330.tw&json=1&delay=0'
response = requests.get(url, headers = {'User-Agent': ua.random})  # response.text為json格式
dict = json.loads(response.text)    # 把json格式轉換為Python的dictionary
info = dict['msgArray'][0]
stock = []
stock.append(info['c'])    # 股票代號
stock.append(info['d'])    # 日期
stock.append(info['t'])    # 時間
stock.append(float(info['v']) * 1000)  # 成交股數 (上市)
stock.append(0) #成交金額 
stock.append(info['o'])    # 開盤價
stock.append(info['h'])    # 最高價
stock.append(info['l'])    # 最低價
stock.append(0 if info['z'] == '-' else float(info['z']))   # 收盤價
stock.append(0 if info['z'] == '-' else float(info['z']) - float(info['y']))    # 漲跌價差
stock.append(0) # 成交筆數
print(stock)    # 請自己注意存入的類型和格式
# 20230306 print出來的結果
# ['2330', '20230306', '13:30:00', 21846000.0, 0, '520.0000', '524.0000', '517.0000', 521.0, 5.0, 0]