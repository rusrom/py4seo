from selenium import webdriver
from random import randint
from time import sleep

chromedriver_path = '/home/rusrom/webdrivers/chromedriver'
geckodriver_path = '/home/rusrom/webdrivers/geckodriver'

# Init Chrome webdriver
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
options.add_argument('start-maximized')
options.add_argument('user-agent=Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18')

browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# Init Firefox webdriver 
# options = webdriver.FirefoxOptions()
# browser = webdriver.Firefox(executable_path=geckodriver_path, options=options)

# Go to URL
browser.get('https://whoer.net/')
sleep(10)

browser.close()
