#coding = utf-8
import datetime
import time
from selenium import webdriver

driver = webdriver.Chrome()

# today:
time.sleep(15)
driver.get('http://oa.koudaikj.com/index.php?m=&c=clock&a=sign')

mobile_tel = driver.find_element_by_id('mobile_tel')
mobile_tel.send_keys('15317076130')

password = driver.find_element_by_id('password')
password.send_keys('August208068')

login_btn = driver.find_element_by_id('login_btn')
time.sleep(2)
login_btn.click()
now = datetime.datetime.now()
now.strftime('%Y-%m-%d %H:%M:%S')
str = "logtime: {}".format(now) + "\n"
with open("card.txt", "a") as f:
    f.write(str)
driver.quite()
