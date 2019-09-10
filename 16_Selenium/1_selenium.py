from selenium import webdriver

chromedriver_path = '/home/rusrom/webdrivers/chromedriver'
geckodriver_path = '/home/rusrom/webdrivers/geckodriver'

# browser = webdriver.Chrome(executable_path=chromedriver_path)
options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(executable_path=geckodriver_path, options=options)
