# VirusTotalUploader
Upload an entire directory of files to virustotal.com and then pull down the results

In order to utilize this service, you need to procure an API Key from https://www.virustotal.com
There is no charge for basic API access, however, the basic API rate limits the number of files that can be uploaded.
Within the upload script, vtfilescan.py, there is a delay built inbetween files to ensure the rate limiting will not
prevent the script from uploading all files. If you purchase a professional API key, you can comment out the delay function.

Prior to Running:

Input API Key into each python script. Set the working directory for your malware repository in vtfilescan.py

TO RUN:

python3 vtfilescan.py   

output:
hashes.txt - list of all hashes that have been uploaded to Virus Total 
file_log.txt - correlated filenames and hashes 



TO RUN:
python3 vtpullresult.py 

output:
All results to standard out.  

