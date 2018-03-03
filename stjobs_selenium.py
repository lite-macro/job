from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# chrome
import os, time
from selenium import webdriver
cwd = os.getcwd() + '/'
driver = webdriver.Chrome('C:/Users/ak66h_000/Downloads/chromedriver.exe')
url = 'http://www.stjobs.sg/singapore-jobs/information-technology-_-it-software-development-jobs/'
driver.get(url)
l = driver.find_elements_by_xpath("//a[@class='text-right pull-right margin-bottom-10']")
l[4].click()
l = driver.find_elements_by_xpath("//a[@class='text-right pull-right margin-bottom-10']").click()
