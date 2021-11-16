import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument('headless')
service = Service("C:\\Users\\radet\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://wwin.com/sports/#f/0/110/0/')
driver.find_element(By.ID, "ContentBody_ctl01_ucOffer_ucMenu_ctl22_favTop").click()
driver.implicitly_wait(10)
driver.find_elements(By.ID, "market_110_19").click()
print()
driver.implicitly_wait(10)
time.sleep(2)
element = driver.find_element(By.ID, "110112014")
rows = element.find_elements(By.TAG_NAME, "tr")
for row in rows:
    try:
        data = row.find_elements(By.TAG_NAME, "td")
        if len(data) == 3:
            for field in data:
                print(field.text)
    except:
        pass

