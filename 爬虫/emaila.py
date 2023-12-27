import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import email

class send_email:
    email_from = ''
    email_to = ''
    email_body = ''
    email_heard = ''
    def send_m(body,heard):
        #print('1')
        my_sender = '' #发方email
        my_pass = '' #password
        email_accept = '' #收方email

        ret = True

        try:
            msg = MIMEText(body,'plain','utf-8')
            msg['From'] = formataddr(['测试',my_sender])
            msg['to'] = formataddr(['system',email_accept])
            msg['Subject'] = heard
            #print('2')
            #server = smtplib.SMTP_SSL('smtp.qq.com',465)
            server = smtplib.SMTP_SSL('120.232.69.34',465)
            
            #print('3')
            print('执行开始')
            server.login(my_sender,my_pass)
            server.sendmail(my_sender,email_accept,msg.as_string())
            server.quit()
        except Exception:
            ret = False
        return ret

if __name__ == '__main__':
    e = send_email
    print("执行email模块")
    body = 'hello world'
    heard = '运行提示'
    ret = e.send_m(body,heard)
    if ret:
        print("email send ok")
    else:
        print("email send error")
    print('结束')

   