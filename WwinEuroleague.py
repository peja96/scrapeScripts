import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('w3c', True)
service = Service("C:\\Users\\RadeToprek\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://wwin.com/sports/#f/0/110/0/')
driver.find_element(By.XPATH, "//span[@title='INTERNATIONAL - Euroleague']").click()
driver.implicitly_wait(10)
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()[contains(., 'Number of Points a Player')]]").click()
time.sleep(1)
driver.implicitly_wait(10)
element = driver.find_element(By.ID, "6010112014")
rows = element.find_elements(By.TAG_NAME, "tr")
print(len(rows))
for row in rows:
    data = row.find_elements(By.TAG_NAME, "td")
    if len(data) == 3:
        name = str(data[0].text).split('(')[0][:-1]
        margin = str(data[0].text).split('(')[1][:-1]
        overBet = data[1].text
        overBet = overBet.replace(",", ".")
        underBet = data[2].text
        underBet = underBet.replace(",", ".")
        print(name, margin, overBet, underBet)
        # for field in data:
        #     print(field.text)