#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pdb

smtp_server='smtp.xxx.com'
mail_user'AAA@xxx.com'
mail_pass='Your password' # note to differ SMTP password from log-in password


sender = 'aaa@xxx.com'
receivers = ['bbb@xxx.com>'] 

message = MIMEText(u'This is context.', 'plain', 'utf-8')
message['From'] = Header(u'AAA<aaa@xxx.com>','utf-8')
message['To'] =  Header(u'BBB<bbb@xxx.com>')
subject = u'Python SMTP Test'
message['Subject'] = Header(subject, 'utf-8')

try:
    server = smtplib.SMTP(smtp_server, 25) 
    # server.set_debuglevel(1) # uncomment this to check which error you meet
    server.login(mail_user,mail_pass)  
    server.sendmail(sender, receivers, message.as_string())
    print u'E-mail is sent successfully!'
except smtplib.SMTPException:
    print u'Error: can\'t send an e-mail.'