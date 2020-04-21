import requests
import pandas as pd
import numpy as np
import glob
import re
import os
from io import BytesIO
from datetime import date, timedelta
from urllib.request import urlopen
from zipfile import ZipFile
import time
import  logging
import datetime
import requests
import sys
import subprocess


    
logging.basicConfig(level = logging.INFO, filename = "log.log",format = '%(message)s')


def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('=' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')


def get_git_data():
    if not os.path.exists('data'):
        os.mkdir('data')
        print("Directory ", 'data',  " Created ")


    else:
        path ="data/COVID-19-master.zip"
        zipurl = 'https://github.com/CSSEGISandData/COVID-19/archive/master.zip'
        zipresp = urlopen(zipurl)
        tempzip = open(path, "wb")
        tempzip.write(zipresp.read())
        tempzip.close()
        
        with ZipFile('data/COVID-19-master.zip','r') as zip:
        # zip.printdir() 
            print('Extracting all the files now...') 
        # print(zip.namelist())
            zip.extractall(path="data",members=['COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
                                            'COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv',
                                            'COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
                                            ]) 
            print('Done!') 

    
    
       # https://thispointer.com/python-get-last-modification-date-time-of-a-file-os-stat-os-path-getmtime/
def update_data():
        print("Downloading Data from Hopkins CSSE ....") 
        download('https://github.com/CSSEGISandData/COVID-19/archive/master.zip','data/COVID-19-master.zip')
        get_git_data()
        logging.info(time.ctime()) 

update_data()





#kill the port
print("Initialize port kill")
subprocess.call(["fuser",'-k','8050/tcp'])
print("Mission port complete!")



#restart the server
print("Initialize server up")
# subprocess.call(["python3","run.py","&"])
# print("Mission Server up initiated!")

# subprocess.Popen(["python3","/home/hawkseye/Desktop/DASH-FLASK-ADMIN/run.py","&"], 
#            stdout=subprocess.PIPE, 
#            stderr=subprocess.STDOUT)

# subprocess.Popen(["/usr/bin/python3","/home/hawkseye/Desktop/DASH-FLASK-ADMIN/run.py","&"])


os.system('forever start -c python3 run.py')