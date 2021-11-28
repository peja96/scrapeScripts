import time

from selenium.webdriver.common.by import By
from scrape_scripts.init import get_driver


driver = get_driver()
driver.get('https://meridianbet.ba/sr/kladjenje/ko%C5%A1arka/poeni-igra%C4%8Da/nba')
time.sleep(1)
rows = driver.find_elements(By.TAG_NAME, 'standard-item-info')
print(len(rows))
for row in rows:
    player_name = row.find_element(By.CLASS_NAME, 'away')
    time = row.find_element(By.CLASS_NAME, 'time')
    margin = row.find_elements(By.CLASS_NAME, 'selection')[1]
    over_bet = row.find_elements(By.CLASS_NAME, 'selection-odds')[1]
    under_bet = row.find_elements(By.CLASS_NAME, 'selection-odds')[0]
    print(player_name.text, time.text, margin.text, over_bet.text, under_bet.text)
