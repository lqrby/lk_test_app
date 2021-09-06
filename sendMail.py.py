'''
Author: your name
Date: 2021-09-03 17:03:59
LastEditTime: 2021-09-03 18:03:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/email.py
'''

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time

class Mailer(object):

  def __init__(self,maillist,mailtitle,mailcontent):
    self.mail_list = maillist
    self.mail_title = mailtitle
    self.mail_content = mailcontent
    ##### email服务器配置 #####
    self.mail_host = "smtp.qq.com"
    self.mail_user = "748862180@qq.com"
    self.mail_pass = "mjeigilwlzvxbcfg"
    self.mail_postfix = "qq.com"
 
  def sendMail(self):
    now = int(time.time())  #显示为时间戳
    timeArray = time.localtime(now)
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
    msg = MIMEMultipart()
    msg['Subject'] = currentTime+'哩咔app UI自动化测试报告'
    msg['From'] = me
    msg['To'] = ";".join(self.mail_list)
 
    puretext = MIMEText(''+self.mail_content)
    msg.attach(puretext)
    xlsx_part = MIMEApplication(open('D:/myObject/lk_test_app/Outputs/allure/allure_report/index.html', 'rb').read())
    xlsx_part.add_header('Content-Disposition', 'attachment', filename='example_requests.csv')
    msg.attach(xlsx_part)
    try:
      s = smtplib.SMTP_SSL() #创建邮件服务器对象
      s.connect(self.mail_host) #连接到指定的smtp服务器。参数分别表示smpt主机和端口
      s.login(self.mail_user, self.mail_pass) #登录到你邮箱
      s.sendmail(me, self.mail_list, msg.as_string()) #发送内容
      s.close()
      return True
    except Exception:
      return False
 
 
if __name__ == '__main__':
  mailto_list = ["1640464937@qq.com;748862180@qq.com"] #邮件接收人
  mail_title = '哩咔app UI自动化测试反馈,请及时查看'
  mail_content = '哩咔app UI自动化测试报告出现异常!!!'+"<a href='http://192.168.10.41:64940/index.html'>http://192.168.10.41:64940/</a>"
  mm = Mailer(mailto_list,mail_title,mail_content)
  res = mm.sendMail()
  if res:
    print("发送邮件成功",res)
  else:
    print("发生邮件错误")