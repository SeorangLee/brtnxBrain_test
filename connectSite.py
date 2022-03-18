import selenium
import os
import chromedriver_autoinstaller as AutoChrome
import shutil

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait



# def chromedriver_update():
#     chrome_ver      = AutoChrome.get_chrome_version().split('.')[0]

#     current_list    = os.listdir(os.getcwd()) 			# 현재 경로의 모든 객체들
#     chrome_list = []
#     for i in current_list:
#         path = os.path.join(os.getcwd(), i) 			# 현재 경로의 모든객체의 전체경로
#         if os.path.isdir(path): 				# 그 경로가 폴더인지 확인
#             if 'chromedriver.exe' in os.listdir(path): 		# 폴더면 안에 chromedriver.exe가 있는지 확인
#                 chrome_list.append(i) 				# 있는경우 chrome_list에 추가

#     old_version = list(set(chrome_list)-set([chrome_ver])) 	# 그중에 최신버전은 제외

#     for i in old_version:
#         path = os.path.join(os.getcwd(),i) 			# 구버전이 있는 폴더의 경로 
#     	shutil.rmtree(path) 					# 그 경로 삭제

#     if not chrome_ver in current_list: 				# 최신버전 폴더가 현재 경로에 없으면
#         AutoChrome.install(True) 				# 크롬드라이버 설치
#     else : pass 


def selenium_test():
    chrome_ver = AutoChrome.get_chrome_version().split('.')[0]
    path = os.path.join(os.getcwd(),chrome_ver)
    path = os.path.join(path,'chromedriver.exe')
    print(path)
    URL ='http://211.119.65.122:53080/dashboard'
    driver = webdriver.Chrome(str(path))
    driver.get(url=URL)

    
    while(True):
    	pass
    
    test1 = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/label[1]/input')
    # test1 = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/label[1]/input')
    test2 = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/label[2]/input')
    test3 = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]')

    test1.send_keys('seorang')

selenium_test();

# URL ='http://211.119.65.122:53080/dashboard'

#  options = webdriver.ChromeOptions() 
#  options.add_experimental_option('excludeSwitches', ['enable-logging']) 
#  driver = webdriver.Chrome(options=options) 
      

 
# driver = webdriver.Chrome(r'C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe') ## webdriver 경로 설정
 
# driver.implicitly_wait(3)  ## 암묵적 대기
 
# driver.get(url=URL)  ## 네이버 접속
# chrome_ver = AutoChrome.get_chrome_version().split('.')[0]
# path = os.path.join(os.getcwd(),chrome_ver)
# path = os.path.join(path,'chromedriver.exe')
# print(path)
# URL ='http://211.119.65.122:53080/dashboard'
# driver = webdriver.Chrome(str(path))
# driver.get(url=URL)

# test1 = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/label[1]/input')
# # test1 = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/label[1]/input')
# test2 = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/label[2]/input')
# test3 = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]')

# test1.send_keys('seorang')


# test2.send_keys('seorang1234')
# test3.click()
 
# # sleep(5)
 
# driver.quit()
