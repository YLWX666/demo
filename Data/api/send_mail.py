import smtplib
from email.mime.text import MIMEText

class SendEmail:
    global send_user
    global host
    global password

    send_user = "mushishi_xu@163.com"
    host = "smtp.163.com"
    password = "123456"
    def send_mail(self,user_list,sub,content):
        user = "Mushishi"+"<"+send_user+">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()