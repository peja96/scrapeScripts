from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from pathlib import Path
import os

op = webdriver.ChromeOptions()
op.add_argument('headless')
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
service = Service(os.environ.get('CHROMEDRIVER'))
driver = webdriver.Chrome(service=service)
driver.get('https://www.amsport.bet/sport')
driver.implicitly_wait(10)
element = driver.find_element(By.ID, "SportPretraga")
element.click()
element.send_keys("Euroleague Igra")
search = driver.find_element(By.CLASS_NAME, "pretraga")
img = search.find_element(By.TAG_NAME, "img")
img.click()
print(element.get_attribute("value"))
driver.implicitly_wait(10)
element.click()
driver.implicitly_wait(15)
table = driver.find_element(By.ID, "tabliga_950")
rows = table.find_elements(By.TAG_NAME, "tr")
del rows[0:5]
c = 0
print(len(rows))
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    time = columns[1].text
    name = columns[4].text
    margin = columns[7].text
    underBet = columns[8].text
    overBet = columns[9].text
    print(name)