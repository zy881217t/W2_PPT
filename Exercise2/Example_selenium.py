# Exercise2 - Selenium
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
edge.get("https://www.cmoney.tw/etf/tw/0050") # 抓取該網站台灣50前10的股票

try:
    # 等元件跑完再接下來的動作，避免讀取不到內容
    WebDriverWait(edge, 100).until(EC.visibility_of_all_elements_located((By.XPATH, "//h3[text()='前10大成分股']/following-sibling::div//tbody//tr")))
    top10 = edge.find_elements(By.XPATH,"//h3[text()='前10大成分股']/following-sibling::div//tbody//tr")   
    for stock in top10:    
        print(stock.text.split("\n")[0])    
except TimeoutException as e:
    print(e)    

edge.close()