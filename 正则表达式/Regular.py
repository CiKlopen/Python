import re

# def validate_string(input_string):
#     pattern = r'^[01]+$'  # 正则表达式，表示字符串只能包含0和1
#     match = re.match(pattern, input_string)

#     if match:
#         print(f"字符串 '{input_string}' 符合正则表达式。")
#     else:
#         print(f"字符串 '{input_string}' 不符合正则表达式。")

# # 测试字符串
# test_string = "110010"
# validate_string(test_string)


# import re

def validate_string(input_string):
    pattern_length = r'^(?=.{9}$)'  # 正则表达式，表示字符串中包含字母
    pattern = r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[_@.])[0-9a-zA-Z_@.]{9}$'
    match_length = re.search(pattern_length,input_string)
    match = re.search(pattern, input_string)

    if not match_length:
        print(f"请确认长度")
        length = len(input_string)
        print(length)       
    elif not match:
            print(f"请检查，未包含大小写字母或特殊符号")
    else:   print(f"ok")

    

    # if match:
    #     print(f"字符串 '{input_string}' 含有字母。")
    # else:
    #     print(f"字符串 '{input_string}' 不含有字母。")

# 测试字符串
test_string = "A_1.11dA0"
validate_string(test_string)







# def find_substring_position(main_string, substring):
#     position = main_string.find(substring)
#     if position != -1:
#         print(f"在字符串 '{main_string}' 中找到子字符串 '{substring}'，位置为 {position}。")
#     else:
#         print(f"在字符串 '{main_string}' 中未找到子字符串 '{substring}'。")

# # 测试字符串
        
# main_string = "hello"
# substring_to_find = "ello"
# substring_to_string = "p"


# find_substring_position(main_string, substring_to_find)
# find_substring_position(main_string, substring_to_string)

