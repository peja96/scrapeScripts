from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time as time_for_schedule
import schedule
import logging
import os
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option('w3c', True)
# path = os.environ['CHROMEDRIVER_DIR']
# service = Service(executable_path=path + "/chromedriver")
service = Service("C:\\Users\\radet\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.amsport.bet/sport')
driver.implicitly_wait(10)
# element = driver.find_element_by_xpath("//*[text()[contains(., 'Specijal košarka')]]")
element = driver.find_element(By.ID, "SportPretraga")
logging.info(element)
print(element)
element.click()
element.send_keys("NBA Igra")
search = driver.find_element(By.CLASS_NAME, "pretraga")
img = search.find_element(By.TAG_NAME, "img")
img.click()
print(element.get_attribute("value"))
driver.implicitly_wait(10)
element.click()
driver.implicitly_wait(15)
table = driver.find_element(By.ID, "tabliga_597")
rows = table.find_elements(By.TAG_NAME, "tr")
print(len(rows))
del rows[0:5]
c = 0
print(len(rows))
print(table.find_element(By.ID, "domaci_1125505"))
for row in rows:
    print(row.text)
    columns = row.find_elements(By.TAG_NAME, "td")
    time = columns[1].text
    name = columns[4].text
    margin = columns[7].text
    underBet = columns[8].text
    overBet = columns[9].text
    length = len((name.split("(")[0]))
    name = name[0:length-1]
    print(time, name, margin, underBet, overBet)

