import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pdfkit

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

# # url = 'http://211.119.65.121:3001/reportiframe'
# url = 'http://211.119.65.121:3001/amyloid/11?patientname=DaewoonKim&patientID=21110&DOB=2020.01.01&Sex=-&StudyDate=2015.01.12&StudyDescription=[%C2%B9%E2%81%B8F]Flutemetamol'
# driver = webdriver.Chrome(options=options, executable_path='C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
# driver.get(url)
# html = driver.page_source
# print('html1')
# with open('reportpage44.html', 'w',  encoding='utf-8') as file:
#     file.write(html)
# exit()

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
pdfkit.from_file(r"C:\Users\SierraLee\WorkSpace\selenium\reportpage44.html", r"C:\Users\SierraLee\WorkSpace\selenium\report4.pdf", configuration=config)
# pdfkit.from_file('reportpage33.html', 'sample.pdf')
print('html2')

# response = requests.get(url)

# if response.status_code == 200:
#   html = response.text
#   soup = BeautifulSoup(html, 'html.parser')
#   print(soup)

# else :
#   print(response.status_code)