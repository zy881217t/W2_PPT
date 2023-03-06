# Exercise2 - MSSQL
import pymssql

# 資料庫設定 (dictionary)
db_settings = {
    "host": "127.0.0.1",
    "user": "",
    "password": "",
    "database": "",
    "charset": "utf8"
}

# (selenium) top10存台灣50top10的list
top10 = ['台積電']  # 範例
# (beautifulsoup) stocks存上市上櫃的股票 
stocks = [['2330', '台積電', '上市', '半導體業'], ['9943', '好樂迪', '上市', '觀光事業']] # 範例

# main
try:
    conn = pymssql.connect(**db_settings)   # 連接MSSQL，並使用前面寫好的設定
    query = "INSERT INTO [dbo].[Exercise2] (stock_code, name, type, category, isTaiwan50) VALUES (%s, %s, %s, %s, %s)"    # 要執行的命令
    with conn.cursor() as cursor:
        for stock in stocks:
            cursor.execute(query, (stock[0], stock[1], stock[2], stock[3], 1 if stock[1] in top10 else 0))   # 執行命令
    conn.commit()   # 記得要commit，才會將資訊儲存到資料庫，不然只會暫存到記憶體
    conn.close()
except Exception as e:
    print(e)
