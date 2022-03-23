from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from copy import copy
import string
import random

# options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.notifications": 1
# })
# driver = webdriver.Chrome(chrome_options=options, executable_path='C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
# # driver = webdriver.Chrome(r'C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe', options=options)
# driver.implicitly_wait(3)
# driver.get('http://211.119.65.122:53080/')
# action = ActionChains(driver)

# #1.select data
# upload_table = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/table/tbody/tr[1]""")
# action.double_click(upload_table).perform()
# # action.double_click(on_element = select_btn).perform()

def upload_select_data(driver, action, options):
    try:
        upload_btn = driver.find_element_by_xpath("""//*[@id="menu-label"]""")
        upload_btn.click()
        sleep(0.5)
        upload_table = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/table/tbody/tr[1]""")
        action.double_click(upload_table).perform()
        sleep(1)
        data = {
          "step":3, "title":"upload", "description":"double click table data", "status":True 
        }
    except:
        data = {
          "step":3, "title":"upload", "description":"double click table data", "status":False 
        }
    return data
    

def upload_pacs(driver,options) :
    try:
        # sleep(1.5)
        # worklist_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[1]/div[1]""")
        # worklist_btn.click()
        # upload_btn = driver.find_element_by_xpath("""//*[@id="menu-label"]""")
        # upload_btn.click()
        
        upload_pacs_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div/div[7]""")
        upload_pacs_btn.click() 
# 
        pacs_tracer_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div[2]""")
        pacs_tracer_btn.click()
        pacs_tracer_next_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[3]/div""")
        pacs_tracer_next_btn.click()
        sleep(1)
        Alert(driver).accept()
        sleep(1)
        pacs_studydate_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div[2]/label/input""")
        pacs_studydate_btn.click()
        pacs_studydate_btn.clear()
        pacs_studydate_btn.send_keys('20160601-20160701')
        pacs_studydescription_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div[3]/label/input""")
        pacs_studydescription_btn.send_keys('aaa')
        pacs_search_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div[4]""")
        pacs_search_btn.click()
        pacs_searched_data_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[3]/table/tbody/tr[1]""")
        pacs_searched_data_btn.click()
        pacs_download_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[4]/div""")
        pacs_download_btn.click()
        sleep(3)
        pacs_selected_data_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[3]/div[2]/table/tbody/tr[1]""")
        pacs_selected_data_btn.click()
        pacs_run_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[3]/div[3]/div""")
        pacs_run_btn.click()
        data = {
          "step":4, "title":"upload", "description":"pacs upload", "status":True 
        }

    except:
         data = {
            "step":4, "title":"upload", "description":"pacs upload", "status":False 
        }
    return data