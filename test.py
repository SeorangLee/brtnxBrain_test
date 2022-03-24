from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
# import login_test from "./login_test"

 

# json 파일쓰기 
file_path = "./sample.json"

data = {}
data['logIn'] = []
data['logIn'].append({
    "step1": True,
    "step2": False,
    "step3": True
})
data['logIn'].append({
    "step1": False,
    "step2": True,
    "step3": True
})
print(data)

with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)



# Actions action = new Actions(driver);
DEBUGGER = True
userName = 'seorang'
pw = 'seorang1234'
# options = webdriver.ChromeOptions()
# options.add_argument('window-size=1920,1080')

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(chrome_options=options, executable_path='C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
# driver = webdriver.Chrome(r'C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe', options=options)
 
driver.implicitly_wait(3)
 
driver.get('http://211.119.65.122:53080/')

action = ActionChains(driver)
# driver.get('https://www.naver.com')

print(driver.title)
# Brightonix Imaging - Amyloid

#sign up
# 1. 모든 조건 만족하는 가입 test

# elm_sign_up = driver.find_element_by_xpath("""//*[@id="root"]/div/div[1]/div[2]""")
# elm_sign_up.click()

# sgn_first_name = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[1]/div/input[1]""")
# sgn_first_name.send_keys('seorang')
# sgn_last_name = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[1]/div/input[2]""")
# sgn_last_name.send_keys('lee')

# sgn_username = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[2]/input""")
# sgn_username.send_keys('seorang3')

# sgn_pwd1 = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[3]/input""")
# sgn_pwd1.send_keys('seorang1234')
# sgn_pwd2 = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[4]/input""")
# sgn_pwd2.send_keys('seorang1234')

# sgn_email = driver.find_element_by_xpath("""//*[@id="root"]/div/form/label[5]/input""")
# sgn_email.send_keys('seorang3@brtnx.com')
# sgn_phone = driver. find_element_by_xpath("""//*[@id="root"]/div/form/label[6]/input""")
# sgn_phone.send_keys('123-4567')

# sgn_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/form/button""")
# sgn_btn.click()

# sleep(2)
# Alert(driver).accept()


if DEBUGGER:
    sleep(1.5)
# login 

elm_id = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div[1]/label[1]/input""")
elm_pwd = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div[1]/label[2]/input""")
elm_id.send_keys(userName) 
elm_pwd.send_keys(pw)

license_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/label/input""")
login_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div[1]/div[2]""")

login_btn.click()
Alert(driver).accept()

license_btn.click()
login_btn.click()




# if DEBUGGER:
#     sleep(1.5)

# # upload page 

upload_btn = driver.find_element_by_xpath("""//*[@id="menu-label"]""")
upload_btn.click()

# #1.select data
# upload_table = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/table/tbody/tr[1]""")
# action.double_click(upload_table).perform()
# # action.double_click(on_element = select_btn).perform()

# # 2. pacs
# upload_pacs_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div/div[7]""")
# upload_pacs_btn.click()

# pacs_tracer_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div[2]""")
# pacs_tracer_btn.click()
# pacs_tracer_next_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[3]/div""")
# pacs_tracer_next_btn.click()
# sleep(2)
# Alert(driver).accept()
# sleep(2)
# pacs_studydate_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div[2]/label/input""")
# pacs_studydate_btn.click()
# pacs_studydate_btn.clear()
# pacs_studydate_btn.send_keys('20160601-20211201')
# pacs_studydescription_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div[3]/label/input""")
# pacs_studydescription_btn.send_keys('aaa')
# pacs_search_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div[4]""")
# pacs_search_btn.click()
# pacs_searched_data_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[3]/table/tbody/tr[1]""")
# pacs_searched_data_btn.click()
# pacs_download_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[4]/div""")
# pacs_download_btn.click()
# sleep(5)
# pacs_selected_data_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[3]/div[2]/table/tbody/tr[1]""")
# pacs_selected_data_btn.click()
# pacs_run_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[3]/div[3]/div""")
# pacs_run_btn.click()

# # if DEBUGGER:
# #     sleep(3)


# # 2.view page

view_btn = driver.find_elements_by_xpath("""//*[@id="menu-label"]""")[1]
view_btn.click()
sleep(2)

# # -menu btns test
# view_mip_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[1]/div[2]""")
# view_mip_btn.click()
# sleep(2)
# view_mip_btn.click()

# view_overlay_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[2]/div[2]/img""")
# view_overlay_btn.click()
# sleep(2)
# view_overlay_btn.click()
# # view_overlay_control_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[2]/div[4]/div""")
# # drag_and_drop_by_offset(view_overlay_control_btn, )

# view_line_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[4]/div""")
# view_line_btn.click()
# sleep(1)
# view_line_btn.click()

# view_brain_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[5]/div""")
# view_brain_btn.click()
# sleep(1)
# view_brain_btn.click()

# view_reverse_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[6]/div""")
# view_reverse_btn.click()
# sleep(1)
# view_reverse_btn.click()

# view_colormap_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div""")
# view_colormap_btn.click()
# sleep(1)

# view_colormap_gray = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div/div/div[1]/div""")
# view_colormap_gray.click()
# sleep(1)
# view_reverse_btn.click()
# sleep(1)
# view_reverse_btn.click()

# view_colormap_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div""")
# view_colormap_btn.click()
# sleep(1)

# view_colormap_hot = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div/div/div[2]/div""")
# view_colormap_hot.click()
# sleep(1)
# view_reverse_btn.click()
# sleep(1)
# view_reverse_btn.click()


# view_colormap_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div""")
# view_colormap_btn.click()
# sleep(1)

# view_colormap_jet = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[8]/div/div/div[3]/div""")
# view_colormap_jet.click()
# sleep(1)
# view_reverse_btn.click()
# sleep(1)
# view_reverse_btn.click()

# view_burger_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div""")
# view_burger_btn.click()

# view_burger_report = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div/div/div[1]/div""")
# view_burger_report.click()

# if DEBUGGER:
#     sleep(1.5)

# # 3.report
# report_last_elm = driver.find_element_by_xpath("""//*[@id="root"]/div/div/div[5]/div[2]/div[4]/div[2]""")
# action.move_to_element(report_last_elm).perform()

# report_back_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div/div[1]""")
# report_back_btn.click()

# sleep(3)
# view_burger_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div""")
# view_burger_btn.click()
# view_burger_csv = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div/div/div[2]/div""")
# view_burger_csv.click()

# view_burger_btn.click()
# view_burger_nifti_suvr = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div/div/div[3]/div""")
# view_burger_nifti_suvr.click()

# view_burger_btn.click()
# view_burger_nifti_itens = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div/div[1]/div[1]/div[9]/div/div/div[4]/div""")
# view_burger_nifti_itens.click()


# if DEBUGGER:
#     sleep(1.5)

# # 4.analysis page
analysis_btn = driver.find_elements_by_xpath("""//*[@id="menu-label"]""")[2]
analysis_btn.click()

analysis_burger_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div""")
analysis_last_elm = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/div[3]/div[2]/div[3]/input""")
action.move_to_element(analysis_last_elm).perform()
analysis_burger_btn.click()
analysis_report = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div/div/div[1]/div""")
analysis_report.click()
sleep(1)
report_back_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div/div[1]""")
report_back_btn.click()
sleep(1)
analysis_burger_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div""")
analysis_burger_btn.click()
analysis_csv = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div/div/div[2]/div""")
analysis_csv.click()
analysis_nifti = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div[2]/div/div/div[3]/div""")
analysis_nifti.click()






# select_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[2]/table/tbody/tr[1]/td[1]/div/img""")
# select_btn.click()



# delete_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div/div[6]/div""")
# delete_btn.click()
# sleep(2)
# Alert(driver).accept()




# pacs_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[5]/div/div[1]/div/div[7]""") 
# pacs_btn.click()



 
sleep(10)
 
driver.quit().py

