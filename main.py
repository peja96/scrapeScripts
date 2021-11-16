import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

service = Service("C:\\Users\\radet\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://www.balkanbet.rs/sportsko-kladjenje')

driver.implicitly_wait(10)
element = driver.find_elements(By.CLASS_NAME, "item-label")
driver.implicitly_wait(10)
print(len(element))
driver.implicitly_wait(15)
driver.switch_to.frame(0)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sidebar-sport-row')))
element = driver.find_elements(By.CLASS_NAME, "sidebar-sport-row")
print(len(element))
button = driver.find_element(By.XPATH, "//*[text()[contains(., 'Košarka Igra')]]").click()
print(button.text)
# wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(., 'Košarka Igra')]]")))
# actions = ActionChains(driver)
# actions.move_to_element(button).click(button).perform()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("arguments[0].click();", button)


rows = driver.find_elements(By.CLASS_NAME, "event-row")
print(len(rows))
# for row in rows:
#   columns = row.find_elements_by_tag_name("td")
#   time = columns[1].text
#   name = columns[4].text
#   margin = columns[7].text
#   underBet = columns[8].text
#   overBet = columns[9].text
#   print(time, name, margin, underBet, overBet)
