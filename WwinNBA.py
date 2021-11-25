import time

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
driver.get('https://wwin.com/sports/#f/0/110/0/')
driver.find_element(By.XPATH, "//span[@title='USA - NBA']").click()
driver.implicitly_wait(10)
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()[contains(., 'Number of Points a Player')]]").click()
print()
driver.implicitly_wait(10)
time.sleep(0.1)
element = driver.find_element(By.ID, "110112014")
rows = element.find_elements(By.TAG_NAME, "tr")
for row in rows:
    try:
        data = row.find_elements(By.TAG_NAME, "td")
        if len(data) == 3:
            print(str(data[0].text).split('(')[0][:-1])
            # for field in data:
            #     print(field.text)
    except:
        pass

