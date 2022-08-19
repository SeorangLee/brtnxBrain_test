from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome('C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
driver.get('http://localhost:3000')
sleep(1)

elm_id = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[2]/label/input""")
elm_pwd = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div[2]/label/input""")
elm_id.send_keys('admin') 
elm_pwd.send_keys('admin')
login_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div/div[1]/div[4]/button""")
login_btn.click()

sleep(1)
elm_product = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div/div/div[1]/div""")
elm_product.click()
sleep(1)

#setting page
menu_settingBtn = driver.find_element_by_xpath("""//*[@id="root"]/div[4]/div[1]/div[6]""")
menu_settingBtn.click()
sleep(1)


#random select

#setting default tracer 
import random

setting_tracer = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[' + str(random.randrange(1,5))+']/div[1]/img')
setting_tracer.click()

#setting reference region
#FMM
setting_region = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]')
setting_region.click()
setting_region_item = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div['+ str(random.randrange(1,5)) +']')
setting_region_item.click()
# sleep(1.5)
#FBP
setting_region = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]')
setting_region.click()
setting_region_item = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div['+ str(random.randrange(1,5)) +']')
setting_region_item.click()
# sleep(1.5)
#FBB
setting_region = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[1]')
setting_region.click()
setting_region_item = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div['+ str(random.randrange(1,5)) +']')
setting_region_item.click()
# sleep(1.5)
#FPN
setting_region = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[1]')
setting_region.click()
setting_region_item = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div['+ str(random.randrange(1,5)) +']')
setting_region_item.click()
sleep(1.5)



//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/img
//*[@id="root"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/img