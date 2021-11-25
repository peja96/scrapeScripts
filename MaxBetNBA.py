from selenium import webdriver
import xlsxwriter
# workbook = xlsxwriter.Workbook('hello.xlsx')
# worksheet = workbook.add_worksheet()
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
  print(player_name)
#   worksheet.write(c, 0, date)
#   worksheet.write(c, 1, player_name)
#   worksheet.write(c, 2, margin)
#   c+=1
# workbook.close()