
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
import json
import log
import login_test
import upload_test
import view_test
import analysis_test
import setting_test
from datetime import datetime

now = datetime.now()
current_time  = now.strftime('%Y%m%d_%Hh%Mm%Ss')

# options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
# options.add_argument('window-size=1920x1080')
# options.add_argument('headless')
# options.add_argument("disable-gpu")
driver = webdriver.Chrome('C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
# driver = webdriver.Chrome(chrome_options=options, executable_path='C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
# driver = webdriver.Chrome(r'C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe', options=options)
# driver.implicitly_wait(3)
driver.get('http://localhost:3000')
sleep(1)
# action = ActionChains(driver)



data = []

# 가입
# login_create_account = login_test.signUp(driver, options)
# data.append(login_create_account)
# #test 계정 삭제
# login_delete_account = login_test.remove_test_id(driver,options)
# data.append(login_delete_account)
# print(data)
#로그인
login_login = login_test.login(driver, options)
data.append(login_login)

#제품 선택
login_select_product = login_test.select_product(driver, options)
data.append(login_select_product)

#업로드
# upload_select_data = upload_test.upload_select_data(driver, action, options)
# data.append(upload_select_data)

# upload_pacs = upload_test.upload_pacs(driver,options)
# data.append(upload_pacs)

#뷰
# view_btn = view_test.view_btn(driver,options)
# data.append(view_btn)

# view_burger_btn = view_test.view_burger_btn(driver, action, options)
# data.append(view_burger_btn)

# #어널리시스
# analysis_page = analysis_test.analysis_page(driver, options, action)
# data.append(analysis_page)

# #세팅
# setting_set_conditions = setting_test.setting_set_conditions(driver, options, action)
# data.append(setting_set_conditions)

# setting_mk_roi = setting_test.setting_mk_roi(driver, options, action)
# data.append(setting_mk_roi)

# setting_save = setting_test.setting_save(driver, options, action)
# data.append(setting_save)

# setting_reset = setting_test.setting_reset(driver, options, action)
# data.append(setting_reset)

# setting_reset = setting_test.setting_reset(driver, options, action)
# data.append(setting_reset)




print(data)
log.mkLog(data) #로그파일 생성
log.mkLogToCSV(current_time, data) #csv파일 생성

