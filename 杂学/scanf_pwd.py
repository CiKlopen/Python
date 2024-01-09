
pwd_global = 1

while pwd_global:

    user_input_str = input('hello,please enter password\n')
    
    def a(strr):
        print("你输入的密码是：",strr)

    def check_pwd(pwd,ab):
        global pwd_global
        if pwd == "0":
            print("密码正确")
            pwd_global = 0
            ab(pwd)
        else:
            print("密码错误")
    
    check_pwd(user_input_str,a)



    


