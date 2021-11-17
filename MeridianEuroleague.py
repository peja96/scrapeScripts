from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument('headless')
service = Service("C:\\Users\\Nikola\\Documents\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://meridianbet.ba/sr/kladjenje/ko%C5%A1arka/poeni-igra%C4%8Da/euroleague')
rows = driver.find_elements(By.TAG_NAME, 'standard-item-info')
print(len(rows))
for row in rows:
    element = row.find_element(By.CLASS_NAME, 'away')
    print(element.text)
