import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from scrape_scripts.init import get_driver


driver = get_driver()
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

  print(player_name)
