from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('w3c', True)
service = Service("C:\\Users\\radet\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.maxbet.ba/ibet-web-client/#/home/leaguesWithMatches')
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, "//*[text()[contains(., 'Specijal košarka')]]")
driver.implicitly_wait(10)
element.click()
poeni = driver.find_element(By.XPATH, "//*[text()[contains(., 'Poeni')]]")
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
  underBet = row.find_elements(By.CLASS_NAME, "main-odd")[3].find_element(By.CLASS_NAME, "ng-binding").text
  overBet = row.find_elements(By.CLASS_NAME, "main-odd")[4].find_element(By.CLASS_NAME, "ng-binding").text
  print(date, player_name, overBet, underBet, margin)
#   worksheet.write(c, 0, date)
#   worksheet.write(c, 1, player_name)
#   worksheet.write(c, 2, margin)
#   c+=1
# workbook.close()