import requests
from bs4 import BeautifulSoup
import time
import emaila 


#此脚本可简单修改 用作任一需要监控的网址
#当前可监控的为纯html的网址，JSON的还需要做
#每次根据要取的值或判断的值 因网址网页的不同 每次定义一个函数去执行 这里可做一步步的完善


url = "https://www.tiananmenchenglou.com/index?userType=1 "   #北京天安门城楼的预约地址

e = emaila.send_email   #email类的实例化




def log(mess):    #简单构造print函数
    print(mess)


def parse_html(txt_html):   #解析html为dom类型
     log()

def parse_json(txt_json):   #将json格式化
     log()





def get(url):      #构造的http—get的请求方法   用的是 requests的库 返回文本
    response_get = requests.get(url)
    #log(response_get.text) #返回文本


    log(response_get.ok)   #状态码400以下为true 以上为false
    #log(response_get.next) #返回重定向中下一个链接
    #log(response_get.json()) # 返回json对像
    print('cookie :',response_get.cookies)
    #log(response_get.close())
    #log(response_get.content)
    #log(response_get.headers)
    #log(response_get.url)
    log(response_get.status_code)
    status_code = response_get.status_code
    if status_code != 200:
        log('状态不对，停止请求')
        exit()
        return


    return response_get.text  #返回值是请求网址的返回文本

def post():
     log()




#解析


def send_message(body,heard):    #这是通知函数
            ret = e.send_m(body,heard)
            if ret:
                print("email send ok")
            else:
                print("email send error")
                print('结束')







if __name__ == '__main__':
    print("程序只会执行这里")

    


    
    run_status = 1
    
    while run_status:
        soup = BeautifulSoup(get(url),'html.parser')  #这是解析函数
        content = soup.find('li',attrs={'data-year-month' : '2023年10月06日'}).text   #这是查找函数 查找标签为li  属性名 ： value 对应的文本
        if content == '06可预约':
            log('正在发送email')
            send_message('查到票了，抓紧抢','辅助')
            run_status = 0
            break

        else:
            log('名额已无')
            log(content)
            time.sleep(15)
    
    


    log(content)    
    #get(url)



    ###此软件优化方向为
        #代理IP的
        #自动下单
        #查询状态
        #自动登录