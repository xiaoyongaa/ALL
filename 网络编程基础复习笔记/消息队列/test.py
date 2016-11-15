import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender="18761515328@163.com"    #发送者
receiver="18761515328@163.com"  #接受者
smtpserver="smtp.163.com"   #smtp服务器域名
username="18761515328@163.com"
password="a845219"
subject="python"

msg = MIMEText('你好','utf-8')#中文需参数‘utf-8’，单字节字符不需要

msg['Subject']=subject


smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

