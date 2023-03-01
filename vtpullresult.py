#VirusTotal Result downloader 
#Written by coldcoffeecode (small data)

import requests
import json
import datetime
import time
import os

url = 'https://www.virustotal.com/vtapi/v2/file/report'

f = open('hashes.txt')
line = f.readline()
while line:
    bar=line.rstrip()
    foo='{}'.format(bar)
    print(foo)
    params = {'apikey': 'VIRUS_TOTAL_API_KEY_HERE', 'resource': foo}
    response = requests.get(url, params=params)
    foo = response.json()
    bar = json.dumps(foo, indent=2)
    print(bar)
    time.sleep(16)
    line = f.readline()
f.close()

