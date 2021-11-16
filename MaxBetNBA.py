from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option('w3c', True)
service = Service("C:\\Users\\radet\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
print("MAXBET - NBA")
driver.get('https://www.maxbet.ba/ibet-web-client/#/home/leaguesWithMatches')
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, "//*[text()[contains(., 'Specijal košarka')]]")
driver.implicitly_wait(10)
element.click()
poeni = driver.find_element(By.XPATH, "//*[text()[contains(., 'Poeni igrača NBA')]]")
poeni.click()
driver.implicitly_wait(15)
table = driver.find_element(By.ID, "leagues-container")
rows = table.find_elements(By.CLASS_NAME, "home-game")
c = 0
print(len(rows))
for row in rows:
  date = row.find_elements(By.CLASS_NAME, "f-09")[1].text
  player_name = row.find_element(By.CLASS_NAME, "cc-w-teams").text
  margin = row.find_element(By.CLASS_NAME, "border").text
  underBet = row.find_element(By.CLASS_NAME, "ng-binding").text
  list = player_name.split("-")
  print(len(list))
  if (len(list) == 2):
    length = len((player_name.split("-")[0]))
    name = player_name[0:length - 1]
  elif (len(list) == 3):
    length = len((list[0]+list[1]))
    name = player_name[0:length]
  print(name, margin, date)
#   worksheet.write(c, 0, date)
#   worksheet.write(c, 1, player_name)
#   worksheet.write(c, 2, margin)
#   c+=1
# workbook.close()