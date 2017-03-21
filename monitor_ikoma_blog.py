﻿#coding:utf-8
import random
import socket
import urllib2
import cookielib
import hashlib 
import time 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pdb
import re

def sendmail(web):
    mail_host="smtp address" # eg. smtp.126.com
    mail_user="xxxx@126.com" # sender
    mail_pass="your password" 

    sender = 'xxxx@126.com'
    receivers = ['yyyy@163.com'] # receivers

    message = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>Here is the <a href="'+web+'">link</a></p>' +
    '</body></html>', 'html', 'utf-8') # message with a link
    message['From'] = Header(u'Ikoma<xxxx@126.com>', 'utf-8')
    message['To'] =  Header(u'Fans<yyyy@163.com>', 'utf-8')

    subject = 'A new message from Ikoma'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "send e-mail successful"
        return 1
    except smtplib.SMTPException:
        print "Error: can't send an e-mail"
        return 0

'''
# use MD5 to check whether the webside is updated
def md5(value):
    m = hashlib.md5()
    m.update(value)
    return m.hexdigest()
'''
    
class BrowserBase(object): 
    def __init__(self):
        socket.setdefaulttimeout(20)

    def speak(self,name,content):
        print '[%s]%s' %(name,content)

    def openurl(self,url):
        cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        self.opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(self.opener)
        user_agents = [
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
                    ] 
       
        agent = random.choice(user_agents)
        self.opener.addheaders = [("User-agent",agent),("Accept","*/*"),('Referer','http://www.google.com')]
        try:
            res = self.opener.open(url)
            context = res.read()
            relink = '<a href="(.*)" rel="bookmark">(.*)</a>'
            info = re.findall(relink, context)
            webpage = info[0][0]
            return webpage
            # md5_num = md5(context)
            # return md5_num
        except Exception,e:
            return 'ERROR 503'
            # self.speak(str(e)+url)
            # raise Exception

if __name__=='__main__':
    splider=BrowserBase()
    web0 = -1
    while True:
      t = time.strftime('%Y-%m-%d, %H:%M',time.localtime(time.time()))
      web = splider.openurl('http://blog.nogizaka46.com/rina.ikoma/')  
      if web == 'ERROR 503':
          time.sleep(90)
          continue
      if web0!=web:
        if web0 != -1:
          check = sendmail(web)
          if check == 1: # send successful
            web0 = web
        else:
          web0 = web
      else:
        print t+' no update'
      time.sleep(60)
