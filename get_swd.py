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
list_of_names = []
entries = pd.read_csv('Student_Certs_sem1_19.csv')
ids = entries['ID'].values
options = webdriver.ChromeOptions() 
options.add_experimental_option("prefs", {
  "download.default_directory": r"/Users/fenilsuchak/Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome('/Users/fenilsuchak/Desktop/scraping_cte/chromedriver' , chrome_options = options)
driver.get('https://swd.bits-goa.ac.in/')
time.sleep(2)
for elems in ids:
	print(elems)
	driver.find_element_by_id("right_search").click()
	time.sleep(1)
	search_for = driver.find_element_by_name("id")
	search_for.send_keys(elems) #Note wont work for dualites. SQL querying to be added.
	final_search = driver.find_elements_by_xpath("//*[@value='Search']")
	final_search[0].click()
	results = driver.find_elements_by_xpath("//*[@id='contact1']")
	list_of_names.append(results[2].text.title())
print(list_of_names)
assert(len(list_of_names) == len(ids))
np.save('swd_names.npy',list_of_names)
