#1.def关键字
#2.函数名
#3.()
#4.函数体
#5.返回值
'''
def send(x,n):
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.header import Header
        sender = '18761515328@163.com'
        receiver = x
        subject = 'python email test'
        smtpserver = 'smtp.163.com'
        username = '18761515328@163.com'
        password = 'a845219'
        msg = MIMEText( n, 'text', 'utf-8' )
        msg['Subject'] = "主题"
        smtp = smtplib.SMTP()
        smtp.connect( smtpserver )
        smtp.login( username, password )
        smtp.sendmail( sender, receiver, msg.as_string() )
        smtp.quit()
    except:
        return "失败"
    else:
        return "成功"
falg=True
while falg:
    y=input("请输入你要发送人的邮箱：")
    re=send(y,"SB")
    if re=="成功":
        print("发送成功")

    else:
        print("发送失败")
'''

#普通参数
#默认参数
#指定参数
#*  默认将传入的参数，全部房子元组中 f1(*[1,2,2,3,])
#** 默认将传入的参数，全部放在字典中f1(**{1:2,3:4})
#万能参数 *args,**kwarges
'''
def f1(**args):
    print(args,type(args))
#a={"1":"2","2":"3"}
f1(k1=1,k2=2)     #直接的附值
'''

def y(*args,**arg1s):
    print(args,arg1s)

#l=["qwdsad","ddwqeq",3]
l={"das":"dasd","weqw":"xcv"}
y(1,2,3,**l)





































































