# VirusTotalUploader
Upload an entire directory of files to virustotal.com and then pull down the results

In order to utilize this service, you need to procure an API Key from https://www.virustotal.com
There is no charge for basic API access, however, the basic API rate limits the number of files that can be uploaded to one file every 15 seconds.
Within the upload script, vtfilescan.py, there is a delay built inbetween files to ensure the rate limiting will not
prevent the script from encountering an error when attempting to upload files. If you purchase a professional API key, you can comment out the delay function.

Prior to Running:

Input API Key into each python script. Set the working directory for your malware repository in vtfilescan.py

Dependencies:

sudo apt update

sudo apt install python3-pip

pip3 install vt

This code was tested running:

  python3 --version 
  
    Python 3.10.6


Ubuntu 22.04.2 LTS

Release:	22.04

Codename:	jammy



TO RUN:

python3 vtfilescan.py   

output:
hashes.txt - list of all SHA256 hashes that have been uploaded to Virus Total 
file_log.txt - correlated filenames and hashes 



TO RUN:
python3 vtpullresult.py 

output:
All results to standard out. vtpullresult assumes you have a file in the current working directory that is called hashes.txt comprised solely of SHA256 strings. This file does not necessarily have to be created by vtfilescan, which will automatically create the file, so you can test any SHA256 hashes that may have already existed on Virus Total. 

