from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from copy import copy
import string
import random

def analysis_page(driver,options, action):
    try:
        analysis_btn = driver.find_elements_by_xpath("""//*[@id="menu-label"]""")[2]
        analysis_btn.click()

        analysis_last_elm = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[3]/div[2]/div[3]/input""")
        action.move_to_element(analysis_last_elm).perform()

        analysis_burger_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div""")
        
        analysis_burger_btn.click()
        analysis_csv = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div/div/div[2]/div""")
        analysis_csv.click()

        analysis_burger_btn.click()
        analysis_nifti = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div/div/div[3]/div""")
        analysis_nifti.click()
        
        # analysis_burger_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div""")
        analysis_burger_btn.click()
        analysis_report = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div/div/div[1]/div""")
        analysis_report.click()
        sleep(1)
        report_back_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div/div[1]""")
        report_back_btn.click()
        sleep(1)

       
        data = {
          "step":7, "title":"analysis", "description":"analysis page, burger button check", "status":True 
        }
    except:
        data = {
          "step":7, "title":"analysis", "description":"analysis page, burger button check", "status":False 
        }
    return data