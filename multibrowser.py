from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.chrome(r'D:/cromedriver/chromedriver.exe')

driver.get("https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views")

print(driver.title)  # title of the page

driver.close()