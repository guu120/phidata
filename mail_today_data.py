import re
import time

localdate = time.strftime("%Y-%m-%d",time.localtime())

mail = '   datetime               hum  tem  pm25  fo\n'

with open(localdate +'.txt',"r") as f1:
    for line in f1.readlines():
        if 'humidity' in line:
            newline = re.sub('^.*"humidity','{humidity',line)
            m = re.findall('[\d\.]+',newline)
            hum = float(m[0])
            tem = float(m[1])
            pm25 = int(m[2])
            fo = float(m[3])/1000
            if fo > 0.6 or hum < 20 or pm25 > 80:
                tag = 'N'
            else:
                tag = ' '
            mail += tag + '  ' + line[:20] + '  '+ str(hum) + '  '+ str(tem) + '  '+ str(pm25) + '  ' + str(fo) + '\n'

# -*- coding: utf-8 -*-
import urllib.request
import json
import time
import random
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
def sendEmail(mail):
    message = MIMEText(mail, 'plain', 'utf-8') # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass) # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string()) # 发送
        print("sent mail")
    except smtplib.SMTPException as e:

        print(e)
# if __name__ == '__main__':
#     sendEmail()
mail_host = "smtp.163.com" # SMTP服务器

mail_user = "XXXXXXXXXX@163.com" # 用户名

mail_pass = "XXXXXXXXXX" # 授权密码，非登录密码

sender = 'XXXXXXXXXX@163.com' # 发件人邮箱(最好写全, 不然会失败)

receivers = 'XXXXXXXXXX@163.com' # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

title = '【From NANOPI】Air condition of ' + localdate # 邮件主题


# mail = '内容'
# print(mail)
sendEmail(mail)
