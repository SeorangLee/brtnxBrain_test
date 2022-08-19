from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import requests 
# from weasyprint import HTML





driver = webdriver.Chrome('C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
# driver = webdriver.Chrome(chrome_options=options, executable_path='C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
driver.get('http://localhost:3000')
sleep(1)
# driver.find_elements_by_css_selector("*")


elm_id = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[2]/label/input""")
elm_pwd = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div[2]/label/input""")
elm_id.send_keys('dwnusa1') 
elm_pwd.send_keys('imaging2016')
login_btn = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div/div[1]/div[4]/button""")
login_btn.click()

sleep(1)
elm_product = driver.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div/div/div[1]/div""")
elm_product.click()
sleep(1)

menu_upload = driver.find_element_by_xpath("""//*[@id="root"]/div[4]/div[1]/div[3]""")
menu_upload.click()
sleep(1)

select_file = driver.find_element_by_id('44')
select_file.click()
sleep(1)

uploadpage_analysisBtn = driver.find_element_by_xpath("""//*[@id="root"]/div[1]/div/div/div[1]/div/div[1]/div[2]""")
uploadpage_analysisBtn.click()
sleep(1)

analysispage_burgerBtn = driver.find_element_by_xpath("""//*[@id="root"]/div[1]/div/div[1]/div/div[3]/div/div[1]""")
analysispage_burgerBtn.click()
sleep(1)

analysispage_burgerBtn_pdfBtn = driver.find_element_by_xpath("""//*[@id="root"]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[1]""")

analysispage_burgerBtn_pdfBtn.click()
sleep(1)

html = driver.page_source
# fileToWrite = open("reportpage.html", "w")

with open('reportpage.html', 'w',  encoding='utf-8') as file:
    file.write(html)


# HTML('./reportpage.html').write_pdf('./reportpage.pdf')

# fileToWrite(html)
# fileToWrite.close()
# response = requests.get(html)

# # beautifulsoup으로 html 분석

# soup = BeautifulSoup(html, 'html.parser')

# file = open("reportHtml.txt", "w")
# print(soup)