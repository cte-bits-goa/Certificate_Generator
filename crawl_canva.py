import urllib.request, urllib.parse, urllib.error
import lxml.html
import time
from bs4 import BeautifulSoup
import tldextract
import requests
import ssl
import sys
from scrapy.http import FormRequest
from fake_useragent import UserAgent
import json
from selenium import webdriver
from functools import partial
from parsel.selector import Selector
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd 
import numpy as np
entries = pd.read_csv('merged_sem2_17_18.csv')
current_course = sys.argv[1]
names = entries.loc[entries['Course'] == current_course ,'Name '].values
print(names)
names = names + ['Jesus']
options = webdriver.ChromeOptions() 
options.add_experimental_option("prefs", {
  "download.default_directory": r"/Users/fenilsuchak/Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome('/Users/fenilsuchak/Desktop/scraping_cte/chromedriver' , chrome_options = options)

header = {
	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'en-US,en;q=0.9',
	'cache-control':'max-age=0',
	'content-length':'163',
	'content-type':'application/x-www-form-urlencoded',
	'origin':'https://www.canva.com',
	'referer':'https://www.canva.com/login/canva?redirect=%2F',
	'upgrade-insecure-requests':'1',
	'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
driver.get('http://www.canva.com/login')
delay = 5
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'email')))
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")
print("done")
username.send_keys('f20160541@goa.bits-pilani.ac.in')
password.send_keys('Fenil@3510')
driver.find_element_by_xpath("//*[@class='form__submitButton js-form__submitButton button buttonBlock buttonSubmit']").click()
for i,name in enumerate(names):
	name = name.title()
	driver.get("https://www.canva.com/design/DAC4kGq3Lvw/E7bYl2iLHWniESgkLr7-hQ/edit")
	if i == 0:
		elem = driver.find_elements_by_xpath("//*[contains(text(), 'Jesus')]")
		for j,elemo in enumerate(elem):
			try:
				print(i,name)
				elemo.click()
				try:
					time.sleep(2)
					drop_down = driver.find_elements_by_xpath("//*[@class='textInput']")[0].send_keys(name)
					done_button = driver.find_elements_by_xpath("//*[@class='button buttonBlock done']")
					done_button[0].click()
					time.sleep(3)
				except:
					driver.execute_script("arguments[0].innerHTML = '{}'".format(name), elemo)
			except:
				continue
		menu2 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@class='element image hasMedia']")))
		ActionChains(driver).move_to_element(menu2).double_click().perform()
		log_but2 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'button editorActionExport prerollAnimation prerollDelay4')]")))
		log_but2.click()
		log_but3 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'button buttonBlock buttonSubmittable exportPopOver__downloadButton')]")))
		log_but3.click()
		time.sleep(10)
	elif name == 'nan':
		continue
	else:
		elem = driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(names[i-1].title()))
		for j,elemo in enumerate(elem):
			try:
				print(i,name)
				elemo.click()
				try:
					time.sleep(2)
					drop_down = driver.find_elements_by_xpath("//*[@class='textInput']")[0].send_keys(name)
					done_button = driver.find_elements_by_xpath("//*[@class='button buttonBlock done']")
					done_button[0].click()
					time.sleep(3)
				except:
					driver.execute_script("arguments[0].innerHTML = '{}'".format(name), elemo)
			except:
				continue
		menu2 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@class='element image hasMedia']")))
		ActionChains(driver).move_to_element(menu2).double_click().perform()
		log_but2 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'button editorActionExport prerollAnimation prerollDelay4')]")))
		log_but2.click()
		log_but3 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'button buttonBlock buttonSubmittable exportPopOver__downloadButton')]")))
		log_but3.click()
		time.sleep(10)
	print("===================================")


