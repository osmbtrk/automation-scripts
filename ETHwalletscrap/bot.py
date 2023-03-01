from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import re
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://debank.com/profile/0x3ddfa8ec3052539b6c9549f12cea2c295cff5296')
time.sleep(10)
try:
    print('begin')
    inputElement = driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div')
    print('balance:'+inputElement.text)

    inputElement1 = driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/span')
    print('asset 1 balance:'+inputElement1.text)
except:
    print('time out, repeat')
 
