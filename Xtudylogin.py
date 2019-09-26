
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome(executable_path=r"D:\drivers\chromedriver.exe")


def applogin (url, userid, password, inputuser, inputpassword, submitbutton):

    driver.get(url)
    driver.maximize_window()
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, inputuser)))
    driver.find_element_by_xpath(inputuser).send_keys(userid)
    driver.find_element_by_xpath(inputpassword).send_keys(password)
    driver.find_element_by_xpath(submitbutton).click()
    time.sleep(2)

def logout():
    Button = driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/nav/div/div[3]/ul/li/a/i')
    driver.execute_script("arguments[0].scrollIntoView();", Button)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/nav/div/div[3]/ul/li/a/i').click()
    time.sleep(2)
    driver.close()


def CLICK(xpath):
    driver.find_element_by_xpath(xpath).click()




def SETTEXT(xpath,data):
    driver.find_element_by_xpath(xpath).send_keys(data)



def down():
    home = driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/footer/div/nav/ul/li[1]/a')
    driver.execute_script("arguments[0].scrollIntoView();", home)



def dropdown(xpath,value):
    driver.find_element_by_xpath(xpath).click()
    driver.find_element_by_xpath(xpath+'/option[@value="'+value+'"]').click()


def Wait_sec(sec):
    time.sleep(sec)



def SET_DATE(xpath,data):
    element = driver.find_element_by_xpath(xpath)
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    element.send_keys(data)
    element.send_keys(Keys.ENTER)



def GET_TEXT(xpath):
    data = driver.find_element_by_xpath(xpath).text
    return data
