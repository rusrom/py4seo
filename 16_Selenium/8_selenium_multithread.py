from selenium import webdriver
from time import sleep
from concurrent.futures import ThreadPoolExecutor


chromedriver_path = '/home/rusrom/webdrivers/chromedriver'
geckodriver_path = '/home/rusrom/webdrivers/geckodriver'

# Init Chrome webdriver
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('start-maximized')
# options.add_argument('window-size=1920x1080') # optional

def worker():
    browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    # Init Firefox webdriver 
    # options = webdriver.FirefoxOptions()
    # browser = webdriver.Firefox(executable_path=geckodriver_path, options=options)

    # Go to URL
    browser.get('https://py4you.com/')
    sleep(14)
    print(browser.title)
    
    browser.close()

with ThreadPoolExecutor(max_workers=4) as executor:
    for _ in range(4):
        executor.submit(worker)
