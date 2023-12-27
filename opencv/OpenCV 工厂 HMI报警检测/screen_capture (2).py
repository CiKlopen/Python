import time
from PIL import ImageGrab
from emaila import send_email
import numpy as np
import cv2
alarm = 0
run = 1
run_root = 1
img = 'C:/Users/Administrator/Desktop/str.png'
# ss_region = (500, 50, 1900, 1000) #距离左上右下的像素
# ss_img = ImageGrab.grab(ss_region)
# ss_img.save("PILImage.jpg")

import win32api,win32con,win32gui

def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0,name)  #输入软件名字 获取窗口句柄
    print('程序id：',handle)
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle)







def screen_capture(x1,x2,y1,y2):
    ss_region = (x1,x2,y1,y2) #距离左上右下的像素
    ss_img = ImageGrab.grab(ss_region)
    #ss_img.show()
    print('窗口坐标：',x1,x2,y1,y2)
    
    #sava_imgname = "alarm_1"
    print('开始获取报警信息')
    
    ss_img.save('C:/Users/Administrator/Desktop/str.png','PNG')
    print('获取完毕')
    return ss_img

def screen_capture_two(x1,x2,y1,y2):
    ss_region = (x1,x2,y1,y2) #距离左上右下的像素
    ss_img = ImageGrab.grab(ss_region)
    #ss_img.show()
    #print('窗口坐标：',x1,x2,y1,y2)
    
    #sava_imgname = "alarm_1"
    #print('开始获取报警信息')
    
    ss_img.save('C:/Users/Administrator/Desktop/sttr.png','PNG')
    #print('获取完毕')
    #return ss_img


def get_img_alart():    #此函数用于获取报警位置图片，以便更好识别
    x1,x2,y1,y2 = get_window_pos("192.168.1.100 (HMI VNC Server) - RealVNC Viewer")
    if x1 >= 0:
        x1 = x1+380
        x2 = x2+30
        y1 = y1-400
        y2 = y2-550      #x1，y1是x轴 x2，y2是y轴
        img = screen_capture(x1,x2,y1,y2)
        return img
    else:
        print('未找到软件')

#get_img_alart()

def get_img_run():
        x1,x2,y1,y2 = get_window_pos("192.168.1.100 (HMI VNC Server) - RealVNC Viewer")
        if x1 >= 0:
            screen_capture_two(x1,x2,y1,y2)
        else:
            print('未找到软件')

#opencv的判断

def alarm_if_main(alarm):
    
        print()
        # img =  cv2.imread("C:/Users/Administrator/Desktop/str.png")
        # cv2.imshow('1',img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()





#get_img_alart()

        









#get_window_pos("回收站")


def send_alarm(alarm_img):   #发送微信 alarm图片
    e = send_email
    print("执行email模块")
    body = '''
    
    <html><h2>故障出现时间：</h2>
    <p>故障图片:</p>
    <p><img src='cid:image1'><p/>
    </html>
    
    '''
    heard = '故障提示'
    img_abb = alarm_img
    ret = e.send_m(body,heard,img_abb)
    if ret:
        print("email send ok")
    else:
        print("email send error")
    print('结束')




#opencv判断


 

def img_process(img,lower,upper):
    """根据阈值处理图像，提取阈值内的颜色。返回处理后只留下指定颜色的图像（其余为黑色）
        img：原图像；lower：最低阈值；upper：最高阈值"""
    #kernel = np.ones((35, 35), np.uint8)                #创建一个35x35卷积核，卷积核内元素全为1
    #img = cv2.imread(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)          #将BGR图像转化为HSV图像，方便颜色提取
    #Open = cv2.morphologyEx(hsv,cv2.MORPH_OPEN,kernel)  #用卷积核对图像进行形态学开运算操作，去除噪声
    #mask = cv2.inRange(Open, lower, upper) 
    mask = cv2.inRange(hsv, lower, upper)
    img_size = mask.shape  #使用shape函数 获取二值化后的像素点高和宽
    img_h = img_size[0]    #白色像素点的高
    img_w = img_size[1]    #宽
    #print(img_h,img_w)       #开运算得到的图像用阈值进行二值化处理（处理后的结果为在阈值内的部分变为白色，不在阈值内的部分为黑色）
    res = cv2.bitwise_and(img, img, mask = mask)
    #a = img_h+img_w        #二值化处理后的图像与原图进行位与运算（处理后在阈值内的颜色变为原颜色，不在阈值内的部分仍为黑色）
    i = 0
    for a in range(img_h):
        for b in range(img_w):
            if mask[a,b].all() > 0:
                i+=1
    print('检测面积：',i)
    return i


def img_alart_white(img,lower,upper):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    return mask

def gl():  #过滤报警编号 无需所有 221 196
    blob = 0


lower_red = np.array([0, 43, 46])        #为红色设置阈值用来为之后处理图像准备
upper_red = np.array([10, 255, 255])     #h s v 红色阈值
num_b = 5000  #过滤面积
a = 0 #计数参数
alart_num = 0 #过滤参数
#img_process(imga,lower_red,upper_red)
while run_root:   #取run变量来决定是否运行 为后续配合HTML
    #核心代码
     print('第',a,'次运行')
     get_img_alart()
     time.sleep(1)
     imga = cv2.imread('C:/Users/Administrator/Desktop/str.png')
     num_a = img_process(imga,lower_red,upper_red)
     
     if a == 0:
         print('程序开始运行,过滤面积为:',num_b)


     if run == 0:
        time.sleep(5)
        run = 1
     if run == 1:
        #print('run')
       
        if num_a > num_b:   #与设定值比对
            
            print('检测到了，面积为：',num_a)
            imgd = 'C:/Users/Administrator/Desktop/str.png'
            imgx = 'C:/Users/Administrator/Desktop/sttr.png'
            alart_num +=1
            if alart_num > 0:  #预警
                get_img_run()
            if alart_num == 5: #提前获取完全图片
                send_alarm(imgx)
                continue
            elif alart_num == 15:
                print('二次过滤检测完毕')
                #alart_num = 0
                send_alarm(imgx) #发送报警图片
                run = 0
                time.sleep(5)
                continue
            elif alart_num == 25:
                print('二次过滤检测完毕')
                #alart_num = 0
                send_alarm(imgx) #发送报警图片
                run = 0
                time.sleep(5)
                continue
            elif num_a < num_b:
                alart_num = 0
                print('故障已无')
                continue       
            elif alart_num > 30:
                print('错误检测已到上限')
                continue
            else:
                time.sleep(1)
                continue

     a=a+1
     alart_num = 0            
     #time.sleep()
     
     

# cv2.imshow('1',img_process(imga,lower_red,upper_red))
# cv2.waitKey(0)
# cv2.destroyAllWindows()