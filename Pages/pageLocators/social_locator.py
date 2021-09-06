
'''
@File    :  social_locator.py    
@Contact :  fangfang.song@asiainnovations.com

@Modify Time    2021/3/17 5:36 下午    
@Author  :  songfang  
@Version :  1.0
@Desciption : 
'''

from appium.webdriver.common.mobileby import MobileBy as Mb

'''探索的页面元素'''


class SocialPageLocators:

    # 点击派对页签
    party = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/textView' and @text='派对']")
    # 点击游戏标签
    game = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/textView' and @text='游戏']")
    # 点击发现
    find = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/textView' and @text='发现']")
    # 点击PK
    PK = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/textView' and @text='PK']")
    # 点击附近
    nearby = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/textView' and @text='附近']")
    # 点击家族
    family = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/textView' and @text='家族']")
    # 点击短视频
    video = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/textView' and @text='短视频']")
    # # 点击开播按钮...
    # streaming = (Mb.ID, "com.asiainno.uplive:id/ivSendLive")
    # # 知道了
    # roger = (Mb.ID, "com.asiainno.uplive:id/txtOk")
    # #  开始直播
    # Begintolive = (Mb.ID, "com.asiainno.uplive:id/btnStart")
    # # 点击我知道了
    # got_in = (Mb.ID, "com.asiainno.uplive:id/tvOk")
    #
    # # 获取连接成功文案
    # accesstocopy = (Mb.XPATH, "//*[contains(@text,'连接成功')]")
    # # 点击退出直播间按钮
    # quit_1 = (Mb.CLASS_NAME, "android.widget.ImageView")
    # # 确定关闭直播
    # certain = (Mb.ID, "android:id/button1")
    # # 直播页的关闭按钮
    # certain_1 = (Mb.ID, "com.asiainno.uplive:id/btnBackHome")
    # # 开播授权弹窗
    # allow_foreground = (Mb.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")