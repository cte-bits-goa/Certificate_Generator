import urllib.request, urllib.parse, urllib.error
import lxml.html
import time
from bs4 import BeautifulSoup
import tldextract
import requests
import ssl
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
options = webdriver.ChromeOptions() 
#options.add_argument("download.default_directory=/Users/fenilsuchak/Downloads")
options.add_experimental_option("prefs", {
  "download.default_directory": r"/Users/fenilsuchak/Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome('/Users/fenilsuchak/Desktop/scrapy_cte/chromedriver' , chrome_options = options)

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

s = requests.Session()
get_some = s.get('http://www.canva.com/login')
soup = BeautifulSoup(get_some.text,'html.parser')
tags = soup('input')
for tag in tags:
	if tag.get('type',None) == "hidden":
		token = tag.get('value')
		break
for form in soup.find_all('form'):
	print(form.attrs.get('action'))
#print(soup.prettify())
print("===================================")
payload = {
	'csrfToken' : token,
	'email' : '********',
	'password' : '*******'
}
post_some = s.post('https://www.canva.com/login/canva?redirect=%2F',data=payload , headers = header)
#get_now = s.get('http://www.canva.com/login/canva?redirect=%2F')
print(post_some.status_code)
#print("xxxxxxxxxxxxxxxxxxxxxx")
soupy = BeautifulSoup(post_some.text, 'html.parser')
#print(soupy.prettify())
if '*********' in post_some.text:
	print("yes")  #hooooorraaayyy
else:
	print("no")

tags = soupy("a")


#Getting the All design
header2 = {
	'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
designs = s.get('https://www.canva.com/', headers = header2)
soup3 = BeautifulSoup(designs.text,'html.parser')
tago = soup3("a")
print(tago)
#print(soup3.prettify())
print(designs.status_code)
print(s.cookies)
#Selenium to the rescure
driver.get("https://www.canva.com")

for c in s.cookies :
    driver.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})

driver.get("https://www.canva.com")
driver.get("https://www.canva.com/design/DAC4kGq3Lvw/edit")
elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Gohan')]")))
#elem = driver.find_elements_by_xpath("//*[contains(text(), 'Gohan')]")
#menu = driver.find_element_by_xpath("//*[contains(@class, 'BITS PILANI K.K. Birla Goa Campus')]")
print(elem)
for i,elemo in enumerate(elem):
	try:
		elemo.click()
		driver.execute_script("arguments[0].innerHTML = 'Dale'", elemo)
	except:
		continue

#print(menu)
#time.sleep(5)
#ActionChains(driver).move_to_element(menu).double_click().perform()
#time.sleep(5)
#try:
#	menu.click()
	#driver.execute_script("arguments[0].innerHTML = 'awarded to'", menu)
#except:
	#pass
#driver.refresh()
#log_but2 = "//button[contains(@class, 'button editorActionExport prerollAnimation prerollDelay4')]"
#driver.find_element_by_xpath(log_but2).click()
#time.sleep(5)
#log_but3 = "//button[contains(@class, 'button buttonBlock buttonSubmittable exportPopOver__downloadButton')]"
#driver.find_element_by_xpath(log_but3).click()
#print(elemento)

# time.sleep(30)

#driver.get("https://download.canva.com/DAC4kGq3Lvw/310/custom/0001-1454498818.png?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27Krishna%2520Kamdi.png&response-expires=Thu%2C%2028%20Jun%202018%2011%3A24%3A26%20GMT&AWSAccessKeyId=AKIAJHKNGJLC2J7OGJ6Q&Expires=1530185066&Signature=P9cDS25Mi9%2FdvUxXO2n%2BODJ0VGI%3D")
