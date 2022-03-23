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

def view_btn(driver,options):
    try:
        view_btn = driver.find_elements_by_xpath("""//*[@id="menu-label"]""")[1]
        view_btn.click()
        
        sleep(5)
        view_mip_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[1]/div[2]""")
        view_mip_btn.click()
        sleep(2)
        view_mip_btn.click()

        view_overlay_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[2]/div[2]/img""")
        view_overlay_btn.click()
        sleep(2)
        view_overlay_btn.click()
        # view_overlay_control_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[2]/div[4]/div""")
        # drag_and_drop_by_offset(view_overlay_control_btn, )

        view_line_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[4]/div""")
        view_line_btn.click()
        sleep(1)
        view_line_btn.click()

        view_brain_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[5]/div""")
        view_brain_btn.click()
        sleep(1)
        view_brain_btn.click()

        view_reverse_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[6]/div""")
        view_reverse_btn.click()
        sleep(1)
        view_reverse_btn.click()

        view_colormap_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div""")
        view_colormap_btn.click()
        sleep(1)

        view_colormap_gray = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div/div/div[1]/div""")
        view_colormap_gray.click()
        sleep(1)
        view_reverse_btn.click()
        sleep(1)
        view_reverse_btn.click()

        view_colormap_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div""")
        view_colormap_btn.click()
        sleep(1)

        view_colormap_hot = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div/div/div[2]/div""")
        view_colormap_hot.click()
        sleep(1)
        view_reverse_btn.click()
        sleep(1)
        view_reverse_btn.click()


        view_colormap_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div""")
        view_colormap_btn.click()
        sleep(1)

        view_colormap_jet = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div/div/div[3]/div""")
        view_colormap_jet.click()
        sleep(1)
        view_reverse_btn.click()
        sleep(1)
        view_reverse_btn.click()
        sleep(2)


        data = {
          "step":5, "title":"view", "description":"view button ", "status":True 
        }
    except:
        data = {
          "step":5, "title":"view", "description":"view button ", "status":False 
        }
    return data
    

def view_burger_btn(driver, action, options):
    try:
        view_burger_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div""")
        view_burger_btn.click()
        view_burger_csv = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div/div/div[2]/div""")
        view_burger_csv.click()

        view_burger_btn.click()
        view_burger_nifti_suvr = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div/div/div[3]/div""")
        view_burger_nifti_suvr.click()

        view_burger_btn.click()
        view_burger_nifti_itens = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div/div/div[4]/div""")
        view_burger_nifti_itens.click()

        view_burger_btn.click()
        view_burger_report = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div/div/div[1]/div""")
        view_burger_report.click()
        sleep(1.5)
        report_last_elm = driver.find_element_by_xpath("""//*[@id="root"]/div/div/div[5]/div[2]/div[4]/div[2]""")
        action.move_to_element(report_last_elm).perform() 
        report_back_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div/div[1]""")
        report_back_btn.click()
        sleep(3)
        data = {
          "step":6, "title":"view", "description":"view burger button ", "status":True 
        }
    except:
        data = {
          "step":6, "title":"view", "description":"view burger button ", "status":False 
        }
    return data