import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option('w3c', True)
path = os.environ['CHROMEDRIVER_DIR']
service = Service(executable_path=path + "/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
print("MOZZART - NBA")
driver.get('https://www.mozzartbet.ba/bs/kladjenje-2018#/?sid=2')
driver.find_element(By.XPATH, "//*[text()[contains(., 'NBA  -  IGRAČI')]]").click()
time.sleep(1)
table = driver.find_elements(By.CLASS_NAME, "competition")[0]
rows = table.find_elements(By.TAG_NAME, "article")
for row in rows:
    time = row.find_element(By.CLASS_NAME, "time").text
    part1 = row.find_element(By.CLASS_NAME, "part1")
    pairs = part1.find_element(By.CLASS_NAME, "pairs")
    playerName = pairs.find_elements(By.TAG_NAME, "span")[1].text
    part2 = row.find_element(By.CLASS_NAME, "part2")
    spans = part2.find_elements(By.TAG_NAME, "span")
    print(time, playerName, spans[2].text, spans[4].text, row.find_element(By.CLASS_NAME, "odds").text)