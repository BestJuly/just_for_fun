#coding=utf-8
import itchat
from itchat.content import *
import pdb
global name

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], True, False, False) # get text and send to XiaoIce
def send_xiaoice(msg):
  global name
  name = msg['FromUserName']
  itchat.send(msg['Text'],toUserName='xiaoice-ms')
  
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], True, False, False) # get img and send to XiaoIce
def send_xiaoice(msg):
  global name
  name = msg['FromUserName']
  msg['Text'](msg['FileName'])
  itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), toUserName='xiaoice-ms')

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], False, False, True) # get text and send to Sender
def send_reply(msg):
  global name
  itchat.send(msg['Text'],name)

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], False, False, True) # get img and send to Sender
def send_xiaoice(msg):
  global name
  msg['Text'](msg['FileName'])
  itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), name)

itchat.auto_login(hotReload=True)
itchat.run()