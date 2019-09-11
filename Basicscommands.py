from selenium import webdriver
from selenium.webdriver.common.keys import Keys




driver=webdriver.Chrome(executable_path=r"D:\drivers\chromedriver.exe")

driver.get("http://beta.xtudy.xyz")


print(driver.title)  #title of the page
print(driver.current_url) # get the current url

driver.close()

import time

usernameinput=".//input[@name='username']"
usernamevalue="admin33"
passwordinput=".//input[@name='password']"
passwordvalue="kickme"


# crome

driver= webdriver.Chrome(executable_path=r"D:\drivers\chromedriver.exe")
driver.get("http://beta.xtudy.xyz")
driver.fullscreen_window()

time.sleep(5)
driver.find_element_by_xpath(usernameinput).send_keys(usernamevalue)
driver.find_element_by_xpath(passwordinput).send_keys(passwordvalue)
driver.find_element_by_xpath(".//button[contains(text(),'go')]").click()

time.sleep(5)


driver.find_element_by_xpath(".//p[contains(text(),'Admission')]").click()
driver.find_element_by_xpath("//*[@id='admission']/ul/li[1]/a").click()

#driver.find_element_by_xpath(".//h3[contains(text(),'Add Student profile')]").send_keys(Keys.ARROW_DOWN * 5)

driver.find_element_by_xpath(".//input[@name='uid']").send_keys("12345xyz")
driver.find_element_by_xpath(".//input[@name='name']").send_keys("bablu Ranjan")
driver.find_element_by_xpath(".//span[contains(text(),'Select a class')]").click()
driver.find_element_by_xpath(".//span[contains(text(),'II')]").click()
driver.find_element_by_xpath(".//input[@name='rollNumber']").send_keys("234")
driver.find_element_by_xpath(".//select[@name='isBus']").click()
driver.find_element_by_xpath(".//select[@name='isBus']/option[1]").click()
driver.find_element_by_xpath(".//input[@name='next']").click()

print (driver.current_url)

driver.close()

