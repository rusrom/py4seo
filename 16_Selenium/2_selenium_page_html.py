from selenium import webdriver
from random import randint
from time import sleep


chromedriver_path = '/home/rusrom/webdrivers/chromedriver'
geckodriver_path = '/home/rusrom/webdrivers/geckodriver'

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

# Get HTML page sourse
page_html = browser.page_source
print(page_html)

browser.close()
