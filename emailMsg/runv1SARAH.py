from selenium import webdriver as web

from selenium.webdriver.common.keys import Keys

import time

import random

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager as CM

import pandas as pd

import gspread

from oauth2client.service_account import ServiceAccountCredentials
import json

noms = ["Nom","Nom"]
prenoms = ["Nom","Nom"]
linkprofiles = ["Nom","Nom"]
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("aaat.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Results SARAH - Scrapping ").sheet1  # Open the spreadhseet
col1 = "Nom"
col2 = "Prenom"
col3 = "Link"
data = pd.DataFrame.from_dict({col1:noms,col2:prenoms,col3:linkprofiles},orient='index')
data.transpose()
data_list = data.values.tolist()
sheet.insert_cols(data_list)
time.sleep(random.randrange(3, 5))
print(' Successfullyy data save!')


				#	https://docs.google.com/spreadsheets/d/1rIV7RAQyh-KCOHXQPRwrs8suXHZ4nkKcOmI0s5_dtCI/edit?usp=sharing

					





