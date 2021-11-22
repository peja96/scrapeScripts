import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from pathlib import Path
import os

op = webdriver.ChromeOptions()
op.add_argument('headless')
dotenv_path = Path('env.env')
load_dotenv(dotenv_path=dotenv_path)
service = Service(os.environ.get('CHROMEDRIVER'))
driver = webdriver.Chrome(service=service)
driver.get('https://meridianbet.ba/sr/kladjenje/ko%C5%A1arka/poeni-igra%C4%8Da/nba')
time.sleep(1)
rows = driver.find_elements(By.TAG_NAME, 'standard-item-info')
print(len(rows))
for row in rows:
    element = row.find_element(By.CLASS_NAME, 'away')
    print(element.text)
