from selenium.webdriver.common.by import By
from scrape_scripts.init import get_driver


driver = get_driver()
driver.get('https://www.amsport.bet/sport')
driver.implicitly_wait(10)
element = driver.find_element(By.ID, "SportPretraga")
element.click()
element.send_keys("NBA Igra")
search = driver.find_element(By.CLASS_NAME, "pretraga")
img = search.find_element(By.TAG_NAME, "img")
img.click()
print(element.get_attribute("value"))
driver.implicitly_wait(10)
element.click()
driver.implicitly_wait(15)
table = driver.find_element(By.ID, "tabliga_597")
rows = table.find_elements(By.TAG_NAME, "tr")
del rows[0:5]
c = 0
print(len(rows))
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    time = columns[1].text
    name = columns[4].text
    margin = columns[7].text
    underBet = columns[8].text
    overBet = columns[9].text
    print(name)
