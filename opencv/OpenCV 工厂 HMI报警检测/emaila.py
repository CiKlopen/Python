import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import email

class send_email:
    email_from = ''
    email_to = ''
    email_body = ''
    email_heard = ''
    def send_m(body,heard,img_path):  #新加附件图片传输功能 传入img
                                      #再次更新 邮件直接加入图片 附件功能已注释
        #img_path = 'C:/Users/Administrator/Desktop/sttr.png'
        my_sender = ''
        my_pass = ''
        email_accept = ''

        ret = True

        try:
            #msg = MIMEMultipart('related')
            msg = MIMEMultipart('related')
            m = MIMEMultipart('alternative')

            msg.attach(m)
            
            
            #msg_a = MIMEText(body,_subtype='html',_charset='utf-8')
            msg['From'] = formataddr(['码垛机',my_sender])
            msg['to'] = formataddr(['system',email_accept])
            msg['Subject'] = heard
            server = smtplib.SMTP_SSL('183.47.101.192',465)
            #msg.attach(msg_a)
            att1_img =img_path
            #img1 = MIMEImage(open(att1_img,'rb').read(),att1_img.split('.')[-1])
            m.attach(MIMEText(body,'html','utf-8'))
            img1 = open(att1_img,'rb')
            msg_image=MIMEImage(img1.read())
            img1.close()
            #img1.add_header('Content-Disposition','attachment',filename=att1_img)
            msg_image.add_header('Content-ID','<image1>')
            msg.attach(msg_image)
            
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
    body = '''
    
    <html><h2>故障出现时间：</h2>
    <p>故障图片:</p>
    <p><img src='cid:image1'><p/>
    </html>
    
    '''
    heard = '故障提示'
    imgab = 'C:/Users/Administrator/Desktop/sttr.png'
    ret = e.send_m(body,heard,imgab)
    if ret:
        print("email send ok")
    else:
        print("email send error")
    print('结束')

   