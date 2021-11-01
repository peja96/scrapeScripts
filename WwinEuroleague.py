import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument('headless')
service = Service("C:\\Users\\Nikola\\Desktop\\SpringScrape\\scrape\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://wwin.com/sports/#f/0/110/0/')
driver.find_element(By.ID, "ContentBody_ctl01_ucOffer_ucMenu_ctl26_favTop").click()
driver.implicitly_wait(10)
time.sleep(1)
elements = driver.find_elements(By.ID, "market_6010_19")
print(len(elements))
elements[0].click()
time.sleep(1)
driver.implicitly_wait(10)
element = driver.find_element(By.ID, "6010112014")
rows = element.find_elements(By.TAG_NAME, "tr")
print(len(rows))
for row in rows:
    try:
        data = row.find_elements(By.TAG_NAME, "td")
        if len(data) == 3:
            for field in data:
                print(field.text)
    except:
        pass

