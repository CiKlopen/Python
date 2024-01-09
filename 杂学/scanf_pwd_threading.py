import threading
import time
def successful_login_callback():
    for i in range(1000000000000000000000000000):
        
        print("密码正确，这是第 {} 次确认".format(i + 1))

def check_pwd(pwd):
    if pwd == "0":
        print("密码正确")
        # 创建并启动一个新线程来运行successful_login_callback函数
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        threading.Thread(target=successful_login_callback).start()
        # 主线程继续运行并打印执行测试
        print("执行测试")
    else:
        print("密码错误")

while True:
    user_input_str = input('hello, please enter password\n')
    check_pwd(user_input_str)
    if user_input_str == "0":
        break
