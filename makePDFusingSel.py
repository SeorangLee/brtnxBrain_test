import json
from selenium import webdriver

downloadPath = r'C:\Users\SierraLee\WorkSpace\selenium'
appState = {
  "recentDestinations":[
    {
      "id": "Save as PDF",
      "origin" : "local"
    }
  ],
  "selectedDestinationId" : "Save as PDF",
  "version" : 2,
  "isHeaderFooterEnabled": False,
  "isLandscapeEnabled": False,
  "marginsType" :1,
}

profile = {'printing.print_preview_sticky_settings.appState':json.dumps(appState),'savefile.default_directory':downloadPath}

chrome_options = webdriver.ChromeOptions() 
chrome_options.add_experimental_option('prefs', profile) 
chrome_options.add_argument('--kiosk-printing')


driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C://Users//SierraLee//WorkSpace//selenium//99//chromedriver.exe')
pdfPath = r'C:\Users\SierraLee\WorkSpace\selenium'
# driver.get(r'C:\Users\SierraLee\WorkSpace\selenium\reportpage22.html')
driver.get('http://localhost:3000')
# driver.get('http://localhost:3000')
driver.execute_script('window.print();')
