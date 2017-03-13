#coding:utf-8
import hashlib 

def md5(value):
    m = hashlib.md5()
    m.update(value)
    return m.hexdigest()

context = 'context'
# calculate MD5
md5_num = md5(context)
print md5_num