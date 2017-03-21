#coding=utf-8
import itchat

global name

@itchat.msg_register(itchat.content.TEXT, True, False, False)
def send_xiaoice(msg):
  global name
  name = msg['FromUserName']
  itchat.send(msg['Text'],toUserName='xiaoice-ms')
  
@itchat.msg_register(itchat.content.TEXT, False, False, True)
def send_reply(msg):
  global name
  if msg['Text']:
    itchat.send(msg['Text'],name)
  else:
    itchat.send('...',name)

itchat.auto_login(hotReload=True)
itchat.run()