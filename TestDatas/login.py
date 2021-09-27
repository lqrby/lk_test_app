'''
Author: your name
Date: 2021-08-30 10:24:06
LastEditTime: 2021-09-27 18:38:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/TestDatas/login.py
'''
''''''
'''登录的测试用例'''
''' 成功登陆、账号密码正确'''
login_success = [
    # {"username": "13100000052", "password": "k123456","check":True},
    {"username" : "18810798467", "password" : "Ren123456","check" : True}
]

'''错误的密码'''
login_error = [{"username" : "13931054777", "password" : "123456gnnn", "expected" : "您输入的密码有误，请重新输入", "check" : True},
               {"username" : "13931054777", "password" : "1", "expected" : "您输入的密码不符合规定长度，请重新输入", "check" : True}]



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