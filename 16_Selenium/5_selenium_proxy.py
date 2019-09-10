from selenium import webdriver
from random import randint
from time import sleep


chromedriver_path = '/home/rusrom/webdrivers/chromedriver'
geckodriver_path = '/home/rusrom/webdrivers/geckodriver'

# Set proxy
# PROXY = "23.23.23.23:3128"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--proxy-server={PROXY}')
# browser = webdriver.Chrome(executable_path=chromedriver_path , options=chrome_options)

# Init Chrome webdriver
browser = webdriver.Chrome(executable_path=chromedriver_path)

# Init Firefox webdriver 
# options = webdriver.FirefoxOptions()
# browser = webdriver.Firefox(executable_path=geckodriver_path, options=options)

# Go to URL
browser.get('https://www.startpage.com/')
sleep(randint(1, 4))

search_field = browser.find_element_by_xpath('//input[@id="query" and @itemprop="query-input"]')
search_field.send_keys('Python best way random integers')

browser.close()
