from selenium import webdriver
from random import randint
from time import sleep

chromedriver_path = '/home/rusrom/webdrivers/chromedriver'
geckodriver_path = '/home/rusrom/webdrivers/geckodriver'

# Init Chrome webdriver
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('start-maximized')
browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# Init Firefox webdriver 
# options = webdriver.FirefoxOptions()
# browser = webdriver.Firefox(executable_path=geckodriver_path, options=options)

# Go to URL
browser.get('https://www.startpage.com/')
sleep(randint(1, 4))

search_field = browser.find_element_by_xpath('//input[@id="query" and @itemprop="query-input"]')
search_field.send_keys('Python random integers')
sleep(randint(1, 4))

search_button = browser.find_element_by_xpath('//button[@class="search-form__button"]')
search_button.click()

sleep(10)
browser.close()
