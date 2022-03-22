import json
from datetime import datetime

now = datetime.now()
current_time  = now.strftime('%Y%m%d_%Hh%Mm%Ss')

def mkLog (log_data) :
    file_path="./logs/"+current_time+".json"
    with open(file_path, 'w') as outfile:
        json.dump(log_data, outfile, indent=4)
        
