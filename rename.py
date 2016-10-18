# !/usr/bin/env python2
# -*-encoding:utf-8-*-
# rename explicit file, eg. video_frame1.jpg --> a_frame1.jpg
import os,sys

path = os.path.abspath('.')
list = os.listdir(path)
ori_name = 'video'
new_name = 'a'
for line in list:
    if line.split('_')[0]==ori_name:  
        newname = line.replace(ori_name,new_name)
        os.rename(os.path.join(path, line), os.path.join(path, newname))