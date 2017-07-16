# coding:utf-8
import re
import requests
import urllib
import os
# get web context
r = requests.get('http://openaccess.thecvf.com/CVPR2017.py')
data = r.text
# find all pdf links
link_list =re.findall(r"(?<=href=\").+?pdf\">pdf|(?<=href=\').+?pdf\">pdf" ,data)
# your local path to download pdf files
localDir = 'E:\CVPR2017\\'
if not os.path.exists(localDir):
    os.makedirs(localDir)
for url in link_list:
    #seperate file name from url links
    file_name = url.split('/')[2].split('.')[0]
    file_path = localDir + file_name + '.pdf'
    # download pdf files
    try:
        urllib.urlretrieve('http://openaccess.thecvf.com/'+url,file_path)
        print "downloading:"+url+" -> "+file_path  
    except Exception,e:
        continue
print "all download finished"  