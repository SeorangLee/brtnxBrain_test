from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from copy import copy
import string
import random

def setting_set_conditions(driver,options, action):
    try:
        setting_btn = driver.find_elements_by_xpath("""//*[@id="menu-label"]""")[3]
        setting_btn.click()
        setting_atlas_dropdown = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]""")
        setting_atlas_dropdown.click()
        setting_atlas_dropdown_HO = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]""")
        setting_atlas_dropdown_HO.click()
        setting_ref_dropdown_fbp = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]""")
        setting_ref_dropdown_fbp.click()
        setting_ref_dropdown_fbp_wc = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div""")
        setting_ref_dropdown_fbp_wc.click()
        setting_region_checkbox_frontal = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[1]/div[2]/div[3]/div[1]/img""")
        setting_region_checkbox_frontal.click()
        setting_tracer_checkbox_fbp = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/img""")
        setting_tracer_checkbox_fbp.click()
        setting_patientInfo_checkbox_dob = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div[2]/div[3]/div[3]""")
        setting_patientInfo_checkbox_dob.click()
        setting_patientInfo_checkbox_type_date = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div[2]/div[3]/div[5]""")
        setting_patientInfo_checkbox_type_date.click()
        data = {
          "step":8, "title":"setting", "description":"setting ", "status":True 
        }
    except:
        data = {
          "step":8, "title":"setting", "description":"setting ", "status":False 
        }
    return data


def setting_mk_roi(driver,options, action):
    try:
        setting_roi_input = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[1]/div[2]/div[11]/input""")
        setting_roi_input.send_keys('my roi')
        setting_roi_add_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[1]/div[2]/div[11]/div/img""")
        setting_roi_add_btn.click()
        sleep(0.5)
        setting_roi_frontal_precentral = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]""")
        setting_roi_frontal_precentral.click()
        setting_roi_frontal_frontalsup = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]""")
        setting_roi_frontal_frontalsup.click()
        setting_roi_frontal_frontalMid = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[2]/div[2]/div[1]/div[2]/div[3]""")
        setting_roi_frontal_frontalMid.click()
        setting_roi_save_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[3]/div""")
        setting_roi_save_btn.click()

        data = {
          "step":9, "title":"setting", "description":"make user defineded ROI", "status":True 
        }
    except:
        data = {
          "step":9, "title":"setting", "description":"make user defineded ROI", "status":False 
        }
    return data


   

def setting_save(driver,options, action):
    try:
        setting_save_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/label""")
        setting_save_btn.click()
        sleep(0.5)
        Alert(driver).accept()
        data = {
          "step":10, "title":"setting", "description":"save conditions", "status":True 
        }
    except:
        data = {
          "step":10, "title":"setting", "description":"save conditions", "status":False 
        }
    return data



def setting_reset(driver,options, action):
    try:
        setting_reset_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[1]/label""")
        setting_reset_btn.click()
        sleep(0.5)
        Alert(driver).accept()
        data = {
          "step":11, "title":"setting", "description":"reset conditions", "status":True 
        }
    except:
        data = {
          "step":11, "title":"setting", "description":"reset conditions", "status":False 
        }
    return data