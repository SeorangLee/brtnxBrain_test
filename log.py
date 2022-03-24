import json
import csv
import pandas as pd
import openpyxl
from datetime import datetime

now = datetime.now()
current_time  = now.strftime('%Y%m%d_%Hh%Mm%Ss')

def mkLog (log_data) :
    file_path="./logs/jason/"+current_time+".json"
    with open(file_path, 'w') as outfile:
        json.dump(log_data, outfile, indent=4)
        

def mkLogToCSV (current_time, data):
    file_path="./logs/xlsx/"+current_time+".xlsx"
    df = pd.DataFrame(data)
    df.to_excel(file_path)
  

