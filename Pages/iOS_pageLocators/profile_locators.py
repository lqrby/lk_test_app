'''
Author: your name
Date: 2021-09-06 15:59:48
LastEditTime: 2021-09-18 13:25:55
LastEditors: your name
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/iOS_pageLocators/profile_locators.py
'''
from appium.webdriver.common.mobileby import MobileBy as Mb
from TestDatas.iOS_Datas import profileData


class ProfilePage:
    num = profileData.user_name
    # 用户up号
    up_num = (Mb.IOS_PREDICATE, 'label == "Up号："' + num['up_num'] + '"')
    # 分享
    share = (Mb.IOS_PREDICATE, 'label == "profile icon share white"')
    # 更多
    more = (Mb.IOS_PREDICATE, 'abel == "im icon more2"')
    # 私信
    msn = (Mb.IOS_PREDICATE, 'label == "私信"')

