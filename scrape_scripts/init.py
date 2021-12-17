from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from pathlib import Path
import os


def get_driver():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    service = Service(os.environ.get('CHROMEDRIVER'))
    driver = webdriver.Chrome(service=service)
    return driver

