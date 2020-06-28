import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm
import time
import pandas as pd
import logging
import os


def get_creds(instructor_data):
    """
        Helper function that recursively scrapes data
        Args:
            instructor_data : pd.DataFrame of the instructor_data
        Returns:
            instructor_data : modified data
    """
    ids = instructor_data["ID"]
    names = instructor_data["Name"]

    for i in tqdm(range(len(ids))):

        try:
            id_button = driver.find_elements_by_xpath('//*[@id="bitsId"]')[0]
            search_button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/div[4]/i/input")
            id_button.send_keys(ids[i])
            search_button.click()
            name_swd = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[3]/div/table/tbody/tr/td[3]').text 
            if name_swd.lower() != names[i].lower():
                logging.info("Changed {} to {}".format(names[i], name_swd))
                names[i] = name_swd.Title()
        except Exception as err:
            logging.critical("{} occured for while searching the id {}".format(err, names[i]))

    return instructor_data
        
def get_swd(instructor_data, resave=True):

    """
        A function to scrap the names of the Instructors and mentors
        from the swd website.
        Args:
        -----
            instructor_data = csv file containing the instructor data
            resave = (bool, default = True) flag to resave the data scrapped from swd website
        Returns:
        -------
            instructor_data : modified dataframe 
    """

    print("Scrapping in progress")

    pwd = os.getcwd()
    #takes care of windows format
    pwd.replace('\\', '/') 
    filename = pwd + '/scrapper_info.log'
    logging.basicConfig(level=logging.INFO, filename=filename, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    # Scrapper info
    options = Options()
    options.add_argument("--disable-infobars")
    options.set_headless()
    driver = webdriver.Firefox(executable_path="geckodriver", options=options)
    driver.get("https://swd.bits-goa.ac.in/search/")

    # After you get the website, you have to enter your credentials to login
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys("f20190390")
    password.send_keys("ammapappa")
    login = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/button/span")
    login.submit()

    # Click Search bar to go for searches
    search = driver.find_element_by_xpath('//a[contains(@href,"/search")]')
    search.click()

    # Recursively get names
    instructor_data = pd.read_csv(instructor_data)
    instructor_data = get_creds(instructor_data)
    instructor_data.to_csv("instructors.csv")

    return instructor_data
