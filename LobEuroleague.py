import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('w3c', True)
path = os.environ['CHROMEDRIVER_DIR']
service = Service(executable_path=path + "/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.lobbet.me/ibet-web-client/#/home/leaguesWithMatches')
driver.implicitly_wait(10)
time.sleep(5)
actions = ActionChains(driver)
actions.move_by_offset(5, 5).click().perform()
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(2)
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, "//*[text()[contains(., 'Specijal Košarka')]]")
driver.implicitly_wait(10)
element.click()
poeni = driver.find_element(By.XPATH, "//*[text()[contains(., 'Poeni')]]")
poeni.click()
driver.implicitly_wait(15)
table = driver.find_element(By.ID, "leagues-container")
rows = table.find_elements(By.CLASS_NAME, "home-game-match")
c = 0
print(len(rows))
for row in rows:
  date = row.find_elements(By.CLASS_NAME, "f-09")[1].text
  player_name = row.find_element(By.CLASS_NAME, "cc-w-teams").text
  margin = row.find_elements(By.CLASS_NAME, "tip-with-odd")[0].text
  under = row.find_elements(By.CLASS_NAME, "tip-with-odd")[1].text
  over = row.find_elements(By.CLASS_NAME, "tip-with-odd")[2].text
  print(date, player_name, margin, under, over)
