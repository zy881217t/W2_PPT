# Exercise1 - Selenium
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions  # Edge用Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException # Timeout Exception使用
from webdriver_manager.microsoft import EdgeChromiumDriverManager   # 自動下載Edge webdriver module

# main
options = EdgeOptions()
options.add_argument("--headless")  # 執行時不顯示瀏覽器
options.add_argument("--disable-notifications")  # 禁止瀏覽器的彈跳通知
#options.add_experimental_option("detach", True)    # 瀏覽器保持開啟
edge = webdriver.Edge(EdgeChromiumDriverManager().install(), options=options)
edge.get("https://www.wantgoo.com/global/holiday/twse") # 台灣股市休市日網站

try:
    # 等元件跑完再接下來的動作，避免讀取不到內容
    WebDriverWait(edge, 100).until(EC.visibility_of_all_elements_located((By.XPATH, "//tbody[@id='holidays']//th")))
    holidays = edge.find_elements(By.XPATH,"//tbody[@id='holidays']//tr")   # 找出//tbody[@id='holidays']//tr下所有的元素
    for holiday in holidays:    # holiday.text -> 2023/01/02 (一) 中華民國開國紀念日(補假)
        info = holiday.text.split(" ")
        print(info[0], info[2]) # 日期 休市理由
except TimeoutException as e:
    print(e)    

edge.close()