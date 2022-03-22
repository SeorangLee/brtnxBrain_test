from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from copy import copy
import string
import random

# sign up

# 1. 모든 조건 만족하는 가입 test

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(chrome_options=options, executable_path='C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
# driver = webdriver.Chrome(r'C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe', options=options)
driver.implicitly_wait(3)
driver.get('http://211.119.65.122:53080/')
action = ActionChains(driver)


def randomInfo(num):
    alphabat_candidate = string.ascii_letters
    num_candidate = string.digits
    val =""
    for i in range(num):
        val += random.choice(alphabat_candidate)
        val += random.choice(num_candidate)

    return val
    

userName = randomInfo(5)
admin_userName = copy(userName)
pw = randomInfo(9)
email = randomInfo(5)+'@'+randomInfo(5)+'.com'

def signUp() :
    try:
			

      elm_sign_up = driver.find_element_by_xpath("""//*[@id="root"]/div/div[1]/div[2]""")
      elm_sign_up.click()
      sgn_first_name = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[1]/div/input[1]""")
      sgn_first_name.send_keys('seorang')
      sgn_last_name = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[1]/div/input[2]""")
      sgn_last_name.send_keys('lee')
      sgn_username = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[2]/input""")
      sgn_username.send_keys(userName)
      sgn_pwd1 = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[3]/input""")
      sgn_pwd1.send_keys(pw)
      sgn_pwd2 = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[4]/input""")
      sgn_pwd2.send_keys(pw)
      sgn_email = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[5]/input""")
      sgn_email.send_keys(email)
      sgn_phone = driver. find_element_by_xpath("""//*[@id="root"]/div/form/label[6]/input""")
      sgn_phone.send_keys('123-4567')
      sgn_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/form/button""")
      sgn_btn.click()
      sleep(2)
      Alert(driver).accept()
      data = {
          "step":0, "title":"login", "description":"create account", "status":True 
        }

    except:
         data = {
            "step":0, "title":"login", "description":"create account", "status":False 
        }
    return data


def remove_test_id():
	try:
			driver.get("http://211.119.65.122:8000/admin")
			# driver.get('http://211.119.65.122:8000/admin')
			# action = ActionChains(driver)
			admin_id = driver.find_element_by_xpath("""//*[@id="id_username"]""")
			admin_id.send_keys('admin')
			admin_pw = driver.find_element_by_xpath("""//*[@id="id_password"]""")
			admin_pw.send_keys('admin')
			admin_login_btn = driver.find_element_by_xpath("""//*[@id="login-form"]/div[3]/input""")
			admin_login_btn.click()
			users_btn = driver.find_element_by_xpath("""//*[@id="content-main"]/div[3]/table/tbody/tr[2]/th/a""")
			users_btn.click()
			users_search_input = driver.find_element_by_xpath("""//*[@id="searchbar"]""")
			users_search_input.send_keys(admin_userName)
			users_search_btn = driver.find_element_by_xpath("""//*[@id="changelist-search"]/div/input[2]""")
			users_search_btn.click()
			users_checkbox = driver.find_element_by_xpath("""//*[@id="action-toggle"]""")
			users_checkbox.click()
			users_dropdown = driver.find_element_by_xpath("""//*[@id="changelist-form"]/div[1]/label/select""")
			users_dropdown.click()
			users_dropdown_delete = driver.find_element_by_xpath("""//*[@id="changelist-form"]/div[1]/label/select/option[2]""")
			users_dropdown_delete.click()
			users_dropdown_delete_go = driver.find_element_by_xpath("""//*[@id="changelist-form"]/div[1]/button""")
			users_dropdown_delete_go.click()
			users_delete_sure_btn = driver.find_element_by_xpath("""//*[@id="content"]/form/div/input[4]""")
			users_delete_sure_btn.click()
			data = {
            "step":1, "title":"login", "description":"delete account", "status":True 
        }
		
	except:
		data = {
            "step":1, "title":"login", "description":"delete account", "status":False 
        }

	return data	


def login():
	driver.get("http://211.119.65.122:53080/")
	try:
		elm_id = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div[1]/label[1]/input""")
		elm_pwd = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div[1]/label[2]/input""")
		elm_id.send_keys('seorang') 
		elm_pwd.send_keys('seorang1234')

		license_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/label/input""")
		login_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div[1]/div[2]""")

		login_btn.click()
		Alert(driver).accept()

		license_btn.click()
		login_btn.click()
		data = {
            "step":2, "title":"login", "description":"login", "status":True 
        }
	
	except:
		data = {
            "step":2, "title":"login", "description":"login", "status":False 
        }

	return data





