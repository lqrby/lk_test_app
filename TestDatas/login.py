'''
Author: your name
Date: 2021-08-30 10:24:06
LastEditTime: 2021-10-29 18:55:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/TestDatas/login.py
'''
''''''
'''登录的测试用例'''
''' 成功登陆、账号密码正确'''
import random

login_success = [
    # {"username": "13100000052", "password": "k123456", "expected" : "ok", "check" : True},
    {"username" : "18810798467", "password" : "Ren123456", "expected" : "ok", "check" : True}
]

'''错误的密码'''
phones = ["18810798467","15001200238"]
phone = random.choice(phones)
login_error = [
    {"username" : phone, "password" : "123456gn", "expected" : "账号与密码不匹配", "check" : True},
    {"username" : "12331054777", "password" : "k121212", "expected" : "账号不存在", "check" : True}
]



'''qq号码登录'''
qq_login = [
    {"qqName" : "768556993", "qqPassword" : "ren123456", "check" : True}
]


'''微博账号密码登录'''
wb_login = [
    {"wbName" : "15001200238", "wbPassword" : "ren123456", "check" : True}
]

'''微信账号密码登录'''
wx_login = [
    {"wxName" : "888862180", "wxPassword" : "ren123456", "check" : True}
]