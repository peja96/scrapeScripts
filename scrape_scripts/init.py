from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from pathlib import Path
import os


def get_driver():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    dotenv_path = Path('../.env')
    load_dotenv(dotenv_path=dotenv_path)
    service = Service(os.environ.get('CHROMEDRIVER'))
    driver = webdriver.Chrome(service=service)
    return driver

