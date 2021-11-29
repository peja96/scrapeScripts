from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
import json
import logging
import os
from selenium.webdriver.common.by import By
from kafka import KafkaProducer

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('w3c', True)
# path = os.environ['CHROMEDRIVER_DIR']
# service = Service(executable_path=path + "/chromedriver")
service = Service("C:\\Users\\RadeToprek\\Documents\\chromedriver_win32\\chromedriver.exe")
logging.basicConfig(filename="error.log", level=logging.ERROR, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)
bookmaker_list = []
producer = KafkaProducer(bootstrap_servers=['ec2-3-139-95-34.us-east-2.compute.amazonaws.com:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


class Bookmaker:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __init__(self, name, margin, overBet, underBet, time, playerName):
        self.name = name
        self.margin = margin
        self.overBet = overBet
        self.underBet = underBet
        self.time = time
        self.playerName = playerName


def mozzart_nba():
    try:
        print("MOZZART - NBA")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://www.mozzartbet.ba/bs/kladjenje-2018#/?sid=2')
        driver.find_element(By.XPATH, "//*[text()[contains(., 'NBA  -  IGRAČI')]]").click()
        time.sleep(1)
        table = driver.find_elements(By.CLASS_NAME, "competition")[0]
        rows = table.find_elements(By.TAG_NAME, "article")
        for row in rows:
            time_of_game = row.find_element(By.CLASS_NAME, "time").text
            part1 = row.find_element(By.CLASS_NAME, "part1")
            pairs = part1.find_element(By.CLASS_NAME, "pairs")
            playerName = pairs.find_elements(By.TAG_NAME, "span")[1].text
            part2 = row.find_element(By.CLASS_NAME, "part2")
            spans = part2.find_elements(By.TAG_NAME, "span")
            underBet = spans[2].text
            overBet = spans[4].text
            margin = row.find_element(By.CLASS_NAME, "odds").text
            print(time_of_game, playerName, underBet, overBet, margin)
            bookmaker_list.append(
                Bookmaker("MozzartNBA", float(margin), float(overBet),
                          float(underBet), time_of_game, playerName))
        driver.close()
    except Exception as e:
        print("MOZZART - NBA ERROR")


def mozzart_el():
    try:
        print("MOZZART - EL")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://www.mozzartbet.ba/bs/kladjenje-2018#/?sid=2')
        driver.find_element(By.XPATH, "//*[text()[contains(., 'EVROLIGA  -  IGRAČI')]]").click()
        time.sleep(1)
        table = driver.find_elements(By.CLASS_NAME, "competition")[0]
        rows = table.find_elements(By.TAG_NAME, "article")
        for row in rows:
            time_of_game = row.find_element(By.CLASS_NAME, "time").text
            part1 = row.find_element(By.CLASS_NAME, "part1")
            pairs = part1.find_element(By.CLASS_NAME, "pairs")
            playerName = pairs.find_elements(By.TAG_NAME, "span")[1].text
            part2 = row.find_element(By.CLASS_NAME, "part2")
            spans = part2.find_elements(By.TAG_NAME, "span")
            underBet = spans[2].text
            overBet = spans[4].text
            margin = row.find_element(By.CLASS_NAME, "odds").text
            print(time_of_game, playerName, underBet, overBet, margin)
            bookmaker_list.append(
                Bookmaker("Mozzart", float(margin), float(overBet),
                          float(underBet), time_of_game, playerName))
        driver.close()
    except Exception as e:
        print("MOZZART - EL ERROR")


def maxbet_nba():
    try:
        print("MAXBET - NBA")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://www.maxbet.ba/ibet-web-client/#/home/leaguesWithMatches')
        driver.implicitly_wait(10)
        element = driver.find_element(By.XPATH, "//*[text()[contains(., 'Specijal košarka')]]")
        driver.implicitly_wait(10)
        element.click()
        poeni = driver.find_element(By.XPATH, "//*[text()[contains(., 'Poeni igrača NBA')]]")
        poeni.click()
        driver.implicitly_wait(15)
        table = driver.find_element(By.ID, "leagues-container")
        rows = table.find_elements(By.CLASS_NAME, "home-game")
        c = 0
        print(len(rows))
        for row in rows:
            date = row.find_elements(By.CLASS_NAME, "f-09")[1].text
            player_name = row.find_element(By.CLASS_NAME, "cc-w-teams").text
            margin = row.find_element(By.CLASS_NAME, "border").text
            underBet = row.find_elements(By.CLASS_NAME, "main-odd")[3].find_element(By.CLASS_NAME, "ng-binding").text
            overBet = row.find_elements(By.CLASS_NAME, "main-odd")[4].find_element(By.CLASS_NAME, "ng-binding").text
            print(date, player_name, overBet, underBet, margin)
            bookmaker_list.append(
                Bookmaker("MaxBetNBA", float(margin), float(overBet),
                          float(underBet), date, player_name))
        driver.close()
    except Exception as e:
        print("MAXBET - NBA ERROR")


def maxbet_el():
    try:
        print("MAXBET - EL")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://www.maxbet.ba/ibet-web-client/#/home/leaguesWithMatches')
        driver.implicitly_wait(10)
        element = driver.find_element(By.XPATH, "//*[text()[contains(., 'Specijal košarka')]]")
        driver.implicitly_wait(10)
        element.click()
        poeni = driver.find_element(By.XPATH, "//*[text()[contains(., 'Poeni')]]")
        poeni.click()
        driver.implicitly_wait(15)
        table = driver.find_element(By.ID, "leagues-container")
        rows = table.find_elements(By.CLASS_NAME, "home-game")
        c = 0
        print(len(rows))
        for row in rows:
            time_of_game = row.find_elements(By.CLASS_NAME, "f-09")[1].text
            player_name = row.find_element(By.CLASS_NAME, "cc-w-teams").text
            margin = row.find_element(By.CLASS_NAME, "border").text
            underBet = row.find_elements(By.CLASS_NAME, "main-odd")[3].find_element(By.CLASS_NAME, "ng-binding").text
            overBet = row.find_elements(By.CLASS_NAME, "main-odd")[4].find_element(By.CLASS_NAME, "ng-binding").text
            list = player_name.split("-")
            length = len(list[0])
            name = player_name[0: length-1]
            print(time_of_game, name, overBet, underBet, margin)
            bookmaker_list.append(
                Bookmaker("MaxBet", float(margin), float(overBet),
                          float(underBet), time_of_game, player_name))
        driver.close()
    except Exception as e:
        print("MAXBET - el ERROR")


def wwin_nba():
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://wwin.com/sports/#f/0/110/0/')
    driver.find_element(By.ID, "ContentBody_ctl01_ucOffer_ucMenu_ctl27_favTop").click()
    driver.implicitly_wait(10)
    driver.find_elements(By.ID, "market_110_19").click()
    print()
    driver.implicitly_wait(10)
    time.sleep(0.1)
    element = driver.find_element(By.ID, "110112014")
    rows = element.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        try:
            data = row.find_elements(By.TAG_NAME, "td")
            if len(data) == 3:
                for field in data:
                    print(field.text)
        except:
            pass
    driver.close()

# not tested
def wwin_el():
    try:
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
                margin = str(data[0].text).split('(')[1][:-1]
                player_name = str(data[0].text).split('(')[0][:-1]
                over_bet = data[1].text
                under_bet = data[1].text
                print(player_name, margin,
                      over_bet, under_bet)
                bookmaker_list.append(
                    Bookmaker("WWin", float(margin), float(over_bet),
                              float(under_bet), "time_of_game", player_name))
        driver.close()
    except Exception as e:
        print("WWin - el ERROR")
        print(e)


def lob():
    try:
        print("LOB - NBA & Euroleague")
        driver = webdriver.Chrome(service=service, options=chrome_options)
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
            print(date, player_name, margin, under, over)
        driver.close()
    except Exception as e:
        print(e)


def amsport_nba():
    try:
        print("AMSport - NBA")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://www.amsport.bet/sport')
        driver.implicitly_wait(10)
        # element = driver.find_element_by_xpath("//*[text()[contains(., 'Specijal košarka')]]")
        element = driver.find_element(By.ID, "SportPretraga")
        logging.info(element)
        print(element)
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
            length = len((name.split("(")[0]))
            name = name[0:length - 1]
            print(time, name, margin, underBet, overBet)
            bookmaker_list.append(
                Bookmaker("AMSportNBA", float(margin), float(overBet),
                          float(underBet), time, name))
        driver.close()
    except Exception as e:
        print("AMSPORT - NBA ERROR")
        print(e)


#not tested
def amsport_el():
    try:
        print("AMSport - Euroleague")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://www.amsport.bet/sport')
        driver.implicitly_wait(10)
        # element = driver.find_element_by_xpath("//*[text()[contains(., 'Specijal košarka')]]")
        element = driver.find_element(By.ID, "SportPretraga")
        logging.info(element)
        print(element)
        element.click()
        element.send_keys("Euroleague Igra")
        search = driver.find_element(By.CLASS_NAME, "pretraga")
        img = search.find_element(By.TAG_NAME, "img")
        img.click()
        print(element.get_attribute("value"))
        driver.implicitly_wait(10)
        element.click()
        driver.implicitly_wait(15)
        table = driver.find_element(By.ID, "tabliga_950")
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
            length = len((name.split("(")[0]))
            name = name[0:length - 1]
            print(time, name, margin, underBet, overBet)
            bookmaker_list.append(
                Bookmaker("AMSport", float(margin), float(overBet),
                          float(underBet), time, name))
        driver.close()
    except Exception as e:
        print("AMSPORT - EUROLEAGUE ERROR")
        print(e)


# not tested
def meridian_nba():
    try:
        print("Meridian - NBA")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://meridianbet.ba/sr/kladjenje/ko%C5%A1arka/poeni-igra%C4%8Da/nba')
        time.sleep(1)
        rows = driver.find_elements(By.TAG_NAME, 'standard-item-info')
        print(len(rows))
        for row in rows:
            player_name = row.find_element(By.CLASS_NAME, 'away').text
            game_time = row.find_element(By.CLASS_NAME, 'time').text
            margin = row.find_elements(By.CLASS_NAME, 'selection')[1].text
            over_bet = row.find_elements(By.CLASS_NAME, 'selection-odds')[1].text
            under_bet = row.find_elements(By.CLASS_NAME, 'selection-odds')[0].text
            print(player_name, game_time, margin, over_bet, under_bet)
            bookmaker_list.append(
                Bookmaker("MeridianNBA", float(margin), float(over_bet),
                          float(under_bet), time, player_name))
        driver.close()
    except Exception as e:
        print("Meridian - NBA ERROR")
        print(e)


# not tested
def meridian_el():
    try:
        print("Meridian - Euroleague")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get('https://meridianbet.ba/sr/kladjenje/ko%C5%A1arka/poeni-igra%C4%8Da/euroleague')
        time.sleep(1)
        rows = driver.find_elements(By.TAG_NAME, 'standard-item-info')
        print(len(rows))
        for row in rows:
            player_name = row.find_element(By.CLASS_NAME, 'away').text
            game_time = row.find_element(By.CLASS_NAME, 'time').text
            margin = row.find_elements(By.CLASS_NAME, 'selection')[1].text
            over_bet = row.find_elements(By.CLASS_NAME, 'selection-odds')[1].text
            under_bet = row.find_elements(By.CLASS_NAME, 'selection-odds')[0].text
            print(player_name, game_time, margin, over_bet, under_bet)
            bookmaker_list.append(
                Bookmaker("MeridianNBA", float(margin), float(over_bet),
                          float(under_bet), time, player_name))
        driver.close()
    except Exception as e:
        print("Meridian - NBA ERROR")
        print(e)


if __name__ == "__main__":
    while True:
        # mozzart_nba()
        # time.sleep(10)
        # maxbet_nba()
        # time.sleep(10)
        # amsport_nba()
        # time.sleep(10)
        maxbet_el()
        time.sleep(10)
        json_list = [ob.__dict__ for ob in bookmaker_list]
        producer.send('EcTopic', value=json_list)
        print(json_list)
        bookmaker_list.clear()
        json_list.clear()
        # bookmaker_list.clear()
        # json_list.clear()
        # maxbet_el()
        # time.sleep(10)
        # json_list = [ob.__dict__ for ob in bookmaker_list]
        # producer.send('EcTopic', value=json_list)
        # print(json_list)
        # bookmaker_list.clear()
        # json_list.clear()
        # maxbet_nba()
        # time.sleep(20)
        # wwin_nba()
