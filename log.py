import json
import csv
from datetime import datetime

now = datetime.now()
current_time  = now.strftime('%Y%m%d_%Hh%Mm%Ss')

def mkLog (log_data) :
    file_path="./logs/"+current_time+".json"
    with open(file_path, 'w') as outfile:
        json.dump(log_data, outfile, indent=4)
        

def mkLogToCSV (current_time, data):
    file = open(current_time+".csv", "w", encoding='utf-8-sig', newline="")
    writer = csv.DicWriter(file, fieldnames=["Test id", "Test module", "description", "Test Result"])
    writer.writeheader()
    writer.writerows(dicList)
    file.close()

