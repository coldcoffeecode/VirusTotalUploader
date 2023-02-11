#VirusTotal File uploader
#Written by coldcoffeecode

import argparse
import asyncio
import os
import sys
import vt
import requests
import time
import json

report_url = 'https://www.virustotal.com/vtapi/v2/file/report'
scan_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': 'VIRUS_TOTAL_API_KEY_HERE'}

path = 'PATH_TO_FILES_FOR_UPLOADING'
entries = os.listdir(path)
current_path = os.getcwd()
for entry in entries:
    print(entry)
    os.chdir(path) 
    files = {'file': ((entry), open((entry), 'rb'))}
    response = requests.post(scan_url, files=files, params=params)
    foo = response.json()
    bar = json.dumps(foo, indent=2)
    print(bar)
    file_code = (foo['resource']) 
    print(file_code) #prints out just resource from json variable
    os.chdir(current_path) 
    masterlist = open("file_log.txt", "a")
    masterlist.write(entry + " " + file_code + "\n")
    file = open("hashes.txt", "a")
    file.write(file_code + "\n" )
    time.sleep(16)
file.close








