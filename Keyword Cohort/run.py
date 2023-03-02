from selenium import webdriver as web

from selenium.webdriver.common.keys import Keys

import time

import random

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

import gspread

from oauth2client.service_account import ServiceAccountCredentials
import json







    

bot_username = ""

bot_password = ""







# 'usernames' or 'links'




us = ''





class Apptweak():

	def __init__(self, username, password):

		self.username = username

		self.password = password

		options = Options()

		options.add_experimental_option("excludeSwitches", ["enable-logging"])

		self.browser = web.Chrome('C:/Users/osmbt/AppData/Local/Programs/Python/Python310/selenium/webdriver/chromedriver.exe',options=options)

		self.browser.maximize_window()



	def close_browser(self):

		self.browser.close()

		self.browser.quit()



	def login(self):
		browser = self.browser
		try:

			browser.get('https://app.apptweak.com/aso-intelligence?view=followed-apps&workspace=160782')

			time.sleep(random.randrange(3, 5))
			cookie_btn =browser.find_element('id', 'CybotCookiebotDialogBodyButtonAccept')
			cookie_btn.click()
			# Enter username:

			username_input = browser.find_element('xpath', '/html/body/main/div/div/div/div[2]/form/div[1]/input')

			username_input.clear()

			username_input.send_keys(self.username)

			time.sleep(random.randrange(2, 4))

			# Enter password:

			password_input = browser.find_element('xpath', '/html/body/main/div/div/div/div[2]/form/div[2]/input')

			password_input.clear()

			password_input.send_keys(self.password)

			time.sleep(random.randrange(1, 2))

			password_input.send_keys(Keys.ENTER)

			time.sleep(random.randrange(3, 5))

			print(f'[{self.username}] Successfully logged on!')

		except Exception as ex:

			print(f'[{self.username}] Authorization fail')

			self.close_browser()



	def xpath_exists(self, url):

		browser = self.browser

		try:

			browser.find_element_by_xpath(url)

			exist = True

		except NoSuchElementException:

			exist = False

		return exist



	def get_followers(self):

		browser = self.browser
		scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
		creds = ServiceAccountCredentials.from_json_keyfile_name("aaat.json", scope)
		client = gspread.authorize(creds)
		sheet = client.open("Untitled spreadsheet").sheet1 # Open the spreadhseet
		print(' Successfullyy opening file keyword Analysis!')

		links = []
		keywords = []
		volumes = []
		ranks = []
		difficuls = []
		comps = []
		print("ok")
		time.sleep(random.randrange(3, 11))
		total_height = int(browser.execute_script("return document.body.scrollHeight"))
		for i in range(1, total_height, 5):
			browser.execute_script("window.scrollTo(0, {});".format(i))
		time.sleep(random.randrange(2,3))
		links = browser.find_elements('xpath', "//a[@class='table-cell__filler at-link-discreet']")
		# get the original window handle
		print("ok1")
		print(len(links))
		time.sleep(random.randrange(2,3))
		main_window = browser.current_window_handle

			# loop through the links
		for link in links:
			# simulate right-click on the link
			link_url = link.get_attribute("href")
			link_url=str(link_url)
			dotindex = link_url.find("metadata")
			link_url1 = link_url[:dotindex]+"keywords"+link_url[dotindex+8:]
			browser.execute_script("window.open('" + link_url1 + "', 'new_tab');")

			# switch to the new tab
			browser.switch_to.window(browser.window_handles[1])
			ink_url =browser.current_url
			# do some task in the new tab
			print("Current URL:",ink_url)
			time.sleep(random.randrange(2,3))
			element_to_hover = browser.find_element('xpath','/html/body/div[2]/div/main/div[3]/div/section/div[1]/div[1]/div[1]/div/div/div')
			ActionChains(browser).move_to_element(element_to_hover).click().perform()

			
			time.sleep(random.randrange(1, 2))
			try:
				print("search for ranked")
				rm= browser.find_element('xpath',"//span[@class='keyword-list__name' and text()='Ranked']")
				time.sleep(random.randrange(1, 2))
				browser.execute_script("arguments[0].click();", rm)
				print("found ranked")
			except NoSuchElementException:
				print("create new ranked")
				Addbtn = browser.find_element('xpath', '/html/body/div[2]/div/main/div[3]/div/section/div[1]/div[1]/button')
				Addbtn.click()
				inpput = browser.find_element('xpath', '/html/body/div[2]/div/main/div[3]/div/section/div[1]/div[1]/div[3]/div/div[1]/div/form/div/div[1]/input')
				inpput.send_keys('Ranked')
				yellowcolor = browser.find_element('xpath', '/html/body/div[2]/div/main/div[3]/div/section/div[1]/div[1]/div[3]/div/div[1]/div/form/div/div[2]/div/div/label[3]/span')
				yellowcolor.click()
				time.sleep(random.randrange(1, 2))
				creaatebtn = browser.find_element('xpath', '/html/body/div[2]/div/main/div[3]/div/section/div[1]/div[1]/div[3]/div/div[1]/div/form/p/button')
				browser.execute_script("arguments[0].click();", creaatebtn)
				print("created")
			time.sleep(random.randrange(1, 2))
			subHeaderbtn = browser.find_element('xpath', '/html/body/div[2]/div/main/div[3]/div/section/div[3]/div[1]/div[2]/div/div[1]/ul/li[3]/button')
			browser.execute_script("arguments[0].click();", subHeaderbtn)
			time.sleep(random.randrange(1, 2))
			Allbtn = browser.find_element('xpath',"//a[@class='kw-picker-content__nav-link' and text()='All']")
			browser.execute_script("arguments[0].click();", Allbtn)
			time.sleep(random.randrange(1, 2))
			total_height = int(browser.execute_script("return document.body.scrollHeight"))
			for i in range(1, total_height, 5):
					browser.execute_script("window.scrollTo(0, {});".format(i))
			time.sleep(random.randrange(2,3))
			try:
				Analysebtn = browser.find_element('xpath', "//button[@class='at-btn at-btn--perform at-btn--small' and text()='Analyze all']")
				browser.execute_script("arguments[0].click();", Analysebtn)
			except NoSuchElementException:
				print("pass")
			keywordscol= []
			keywordscol = browser.find_elements('xpath', "//div[@class='keyword-label__label']")
			for keycol in keywordscol:
				key = keycol.get_attribute("data-kw-full-name")
				print(key)
				keywords.append(key)
			volumescol= []
			volumescol = browser.find_elements('xpath', "//td[@class='table-cell table-cell--volume']")
			for volcol in volumescol:
				vol = volcol.find_element('xpath', './span').text
				print(vol)
				volumes.append(vol)
			print(len(volumes))
			rankscol= []
			rankscol = browser.find_elements('xpath', "//td[@class='table-cell table-cell--rank']")
			for rankcol in rankscol:
				rank = rankcol.text
				print(rank)
				ranks.append(rank)
			deficultyscol= []
			deficultyscol = browser.find_elements('xpath', "//a[@class='table-cell table-cell--diff']")
			for defcol in deficultyscol:
				defcel = defcol.find_element('xpath', './span').text
				difficuls.append(defcel)
			comps = [a/b for a,b in zip(volumes,difficuls)]
			# close the new tab and switch back to the original tab
			browser.close()
			browser.switch_to.window(main_window)
			values = [keywords,ranks,comps,volumes]
			transposed_values = list(map(list, zip(*values)))
			sheet.batch_update([{
                                'range': f'B20:E{len(keywords)+20}',
                                'values': transposed_values,
                        }])
			print(' Successfullyy insert cols!')
		sheetr = client.open("Untitled spreadsheet").sheet1 # Open the spreadhseet
		print(' Successfullyy opening file keyword Analysis!')
		values = [keywords,ranks,volumes]
		transposed_values = list(map(list, zip(*values)))
		sheetr.batch_update([{
			'range': f'B1:D{len(keywords)}',
			'values': transposed_values,
		}])
		time.sleep(1)




	



bot = Apptweak(bot_username, bot_password)
bot.login()

bot.get_followers()
bot.close_browser()
