'''
Author: your name
Date: 2021-09-06 15:59:48
LastEditTime: 2021-10-15 10:25:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/pageLocators/social_locator.py
'''



from appium.webdriver.common.mobileby import MobileBy as Mb

'''游戏的页面元素'''


class GameLocators:

    # 点击套圈圈
    Trap = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='套圈圈']")
    # 点击全民造车
    AllPeople_buildCars = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='全民造车']")
    # 点击金币套圈
    gold_coin_ferrule = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='金币套圈']")
    # 点击金币造车
    gold_coin_car = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='金币造车']")
    # 点击丛林狩猎
    jungle_hunt = (Mb.XPATH, "//*[@resource-id='com.ourydc.yuebaobao:id/tv_gamename' and @text='丛林狩猎']")



    # 套圈圈断言
    Trap_assert = (Mb.ID, "com.ourydc.yuebaobao:id/rootview")