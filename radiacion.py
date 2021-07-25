
from selenium import webdriver

fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(fp)
url = 'http://www.adrase.ciemat.es/mapa-zona-peninsula/index.php'
driver.get(url)

driver.find_element_by_name("lat_question").send_keys('30')
driver.find_element_by_name("lon_question").send_keys('-3')

