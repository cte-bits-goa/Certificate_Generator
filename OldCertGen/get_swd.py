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
import os
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
from tqdm import tqdm
import sys
if __name__ == "__main__":
	arguments = sys.argv[1:]
	try:
		list_of_names = list(np.load('swd_names.npy'))
	except:
		just_once = []
		np.save('swd_names.npy',just_once)
		list_of_names = list(np.load('swd_names.npy'))

	entries = pd.read_csv(arguments[0])
	names = entries['Name'].values
	ids = entries['ID'].values
	options = webdriver.ChromeOptions() 
	options.add_experimental_option("prefs", {
	  "download.default_directory": r"/Users/fenilsuchak/Downloads",
	  "download.prompt_for_download": False,
	  "download.directory_upgrade": True,
	  "safebrowsing.enabled": True
	})
	with open('position.txt', 'r') as f:
			pos = int(f.read())
	driver = webdriver.Chrome(os.path.abspath('chromedriver') , chrome_options = options)
	driver.get('https://swd.bits-goa.ac.in/')
	time.sleep(2)
	full_pos = pos
	ids_check = ids[full_pos:]
	for i,elems in enumerate(ids_check):
		print(i, names[pos])
		driver.find_elements_by_id("right_search")[0].click()
		time.sleep(3)
		search_for = driver.find_element_by_name("id")
		try:
			search_for.send_keys(elems)
			final_search = driver.find_elements_by_xpath("//*[@value='Search']")
			final_search[0].click()
			results = driver.find_elements_by_xpath("//*[@id='contact1']")
		except:
			list_of_names.append((elems,names[pos]))
			pos = pos+1
			with open('position.txt', 'w') as f:
				f.write('{}'.format(pos))
			np.save('swd_names.npy',list_of_names)
			continue
		list_of_names.append((elems,results[2].text.title()))
		pos = pos+1
		with open('position.txt', 'w') as f:
			f.write('{}'.format(pos))
		np.save('swd_names.npy',list_of_names)
	print(len(list_of_names))
	print(len(ids))
	assert(len(list_of_names) == len(ids))