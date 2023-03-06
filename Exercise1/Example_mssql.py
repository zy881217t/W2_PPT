# Exercise1 - MSSQL
import pymssql
import calendar

# 資料庫設定 (dictionary)
db_settings = {
    "host": "127.0.0.1",
    "user": "",
    "password": "",
    "database": "",
    "charset": "utf8"
}

# 你爬蟲存下來的資訊(存成dictionary，key為日期、value為節日)
holidays = {
    '2023/03/06': '爬蟲上課日'  # 範例
}

# 計算開市日
WorkDays = 0

# main
try:
    conn = pymssql.connect(**db_settings)   # 連接MSSQL，並使用前面寫好的設定
    query = "INSERT INTO [dbo].[Exercise1] (Date, Day_of_stock, Reason) VALUES (%s, %d, %s)"    # 要執行的命令
    with conn.cursor() as cursor:
        for month in range(1, 13):   # 1 ~ 12月
            for day in range(1, calendar.monthrange(2023, month)[1] + 1): # 該月所有日子

                date = f"2023/{month:02d}/{day:02d}"    # 日期存為YYYY/MM/DD格式字串
                weekday = calendar.weekday(2023, month, day)  #取得星期，星期一為0
                
                if date in holidays:  #若日期為特殊假日
                    cursor.execute(query, (date, -1, holidays[date]))
                elif weekday == 5 or weekday == 6:  #若日期為周末(星期六為5，星期日為6)
                    cursor.execute(query, (date, -1, ""))
                else:
                    WorkDays += 1   # 開市日計算
                    cursor.execute(query, (date, WorkDays, ""))

    conn.commit()   # 記得要commit，才會將資訊儲存到資料庫，不然只會暫存到記憶體
    conn.close()
except Exception as e:
    print(e)
