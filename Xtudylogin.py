
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"D:\drivers\chromedriver.exe")
import time


def applogin (url, userid, password, inputuser, inputpassword, submitbutton):

    driver.get(url)
    time.sleep(5)
    driver.find_element_by_xpath(inputuser).send_keys(userid)
    driver.find_element_by_xpath(inputpassword).send_keys(password)
    driver.find_element_by_xpath(submitbutton).click()
    time.sleep(5)
    #if driver.current_url('http://beta.xtudy.xyz/dashboard/dashboard.php'):
    return driver.current_url
    #else:
    #   return 'FAIL'

def logout():
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/nav/div/div[3]/ul/li/a/i').click()
    time.sleep(5)
    #if driver.current_url('http://beta.xtudy.xyz/dashboard/login.php'):
    driver.close()
    return driver.current_url
    #else:
        #return 'fail'
def add_student(admission,add, student_xpath,value):
    driver.find_element_by_xpath(admission).click()
    driver.find_element_by_xpath(add).click()
    driver.find_element_by_xpath(student_xpath).send_keys(value)
