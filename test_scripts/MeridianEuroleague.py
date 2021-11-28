import time

from selenium.webdriver.common.by import By
from scrape_scripts.init import get_driver


driver = get_driver()
driver.get('https://meridianbet.ba/sr/kladjenje/ko%C5%A1arka/poeni-igra%C4%8Da/euroleague')
time.sleep(1)
rows = driver.find_elements(By.TAG_NAME, 'standard-item-info')
print(len(rows))
for row in rows:
    element = row.find_element(By.CLASS_NAME, 'away')
    print(element.text)
