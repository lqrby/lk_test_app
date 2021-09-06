'''
Author: your name
Date: 2021-08-27 16:38:44
LastEditTime: 2021-09-01 13:46:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Pages/pageLocators/login_locators.py
'''
from appium.webdriver.common.mobileby import MobileBy as Mb

'''登录页面元素'''
class LoginPageLocator:
    ##################################哩咔登录相关元素定位###################################
    agree=(Mb.ID,'com.ourydc.yuebaobao:id/btn_ok') #启动app弹出用户协议同意按钮元素
    determine = (Mb.ID,'com.ourydc.yuebaobao:id/tv_sure') #登录时弹出的确认用户协议确定按钮元素

    #账号密码登录元素
    phoneBtn = (Mb.ID,'com.ourydc.yuebaobao:id/btn_login_phone') #手机号登录按钮
    nameAndPassBtn = (Mb.ID,'com.ourydc.yuebaobao:id/tv_account_login') #点击账号密码登录按钮
    username_type = (Mb.ID,'com.ourydc.yuebaobao:id/et_account') #账号（手机号）输入框
    # username_type=(Mb.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.EditText[1]') #账号（手机号）输入框
    password_type = (Mb.ID,'com.ourydc.yuebaobao:id/et_pwd') #密码输入框
    loginBtn = (Mb.ID,'com.ourydc.yuebaobao:id/btn_login') #获取登录按钮
    
    #手机号验证码登录
    et_phone = (Mb.ID,'com.ourydc.yuebaobao:id/et_phone')	#手机号输入框元素
    codeBtn = (Mb.ID,'com.ourydc.yuebaobao:id/btn_get_verification_code') #获取验证码按钮元素
    input_one = (Mb.XPATH, "//*[@class='android.widget.TextView' and @index='0']") # 验证码输入框1
    input_two = (Mb.XPATH, "//*[@class='android.widget.TextView' and @index='1']") # 验证码输入框2
    input_three = (Mb.XPATH, "//*[@class='android.widget.TextView' and @index='2']") # 验证码输入框3
    input_four = (Mb.XPATH, "//*[@class='android.widget.TextView' and @index='3']") # 验证码输入框4
    codeList = [input_one,input_two,input_three,input_four]
    verification_code = (Mb.ID,'com.ourydc.yuebaobao:id/btn_get_verification_code') #重新获取验证码
    #滑块儿验证码


    # maxPicture = (Mb.ID,"com.ourydc.yuebaobao:id/img")
    maxPicture = (Mb.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView[1]")
    yzmBtn = (Mb.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView")



    


    ##################################哩咔登录相关元素定位结束###################################

    #微信登录元素
    wdChatBtn=(Mb.XPATH,"//*[@class='android.widget.ImageView' and @index='0']")
    wdChatNameInput=(Mb.XPATH,"//*[@text='请填写微信号/QQ号/邮箱']")
    bindingPhoneBtn=(Mb.ID,"com.ourydc.yuebaobao:id/bindPhoneBtn") #绑定手机号按钮(微信微博公用)
    #=======================已有登录记录，只需输入密码===========================
    
    ffpBtn=(Mb.ID,"com.tencent.mm:id/ffp") #微信掉线通知确定按钮/微信登录失败确定按钮
    bxzInput=(Mb.ID,"com.tencent.mm:id/bxz") #微信密码输入框
    erpBtn=(Mb.ID,"com.tencent.mm:id/erp") #微信密码按钮(公用)
    erhText=(Mb.ID,"com.tencent.mm:id/erh") #微信用户昵称
    #=======================无登录记录===========================
    we_name=(Mb.XPATH,"//*[@text='请填写微信号/QQ号/邮箱']") #微信账号输入框
    we_pass=(Mb.XPATH,"//*[@text='请填写密码']") #微信密码输入框
    #===========================================================
    ffhText=(Mb.ID,"com.tencent.mm:id/ffh") #微信登录失败提示
    

    #qq登录元素
    qqBtn=(Mb.XPATH,"//*[@class='android.widget.ImageView' and @index='1']")
    qqLoginBtn=(Mb.ID,"com.tencent.mobileqq:id/login") # qq登录按钮
    fdsBtn=(Mb.ID,"com.tencent.mobileqq:id/fds") #qq授权按钮
    otherqqLoginBtn=(Mb.ID,"com.tencent.mobileqq:id/asz") #使用其他QQ账号登录按钮
    downLoadBtnBtn=(Mb.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.widget.Button") #使用其他QQ账号登录
    qqInputNane=(Mb.XPATH,'//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]') #QQ账号输入框
    qqInputPass=(Mb.ID,'com.tencent.mobileqq:id/password') # QQ密码输入框
    qqNamePassErrorBtn=(Mb.ID,'com.tencent.mobileqq:id/dialogText') # QQ用户名或密码提示按钮
    #=======================================================
    #微博登录元素
    # microblogBtn=(Mb.XPATH,"//*[@class='android.widget.ImageView' and @index='2']") #微博图标,此方法获取元素点击无效
    #登录页点击微博的按钮元素
    microblogBtn=(Mb.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.ImageView[3]") #使用微博账号登录元素
    #微博登录页登录按钮元素
    microblog_loginInput=(Mb.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]") #微博登录页用户名输入框元素
    # microblog_loginBtn=(Mb.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]") #微博登录页用户名输入框元素
    microblog_authorizeBtn=(Mb.ID,"com.sina.weibo:id/tvChangeAccount") #微博授权按钮元素
    confirmBtn=(Mb.ID,"com.ourydc.yuebaobao:id/tv_cancel") #微博返回确认按钮元素
    getCodeBtn=(Mb.XPATH,"//android.view.View[@text='获取短信验证码']") #获取短信验证码按钮元素
    jumpCodeBtn=(Mb.XPATH,"//*[@class='android.view.View' and @index='1']") #注册未设置密码跳转到验证码登录按钮元素

    codeInput=(Mb.XPATH,"//*[@class='android.widget.EditText' and @index='0']") #验证码输入元素
    okBtn=(Mb.XPATH,"//*[@class='android.widget.EditText' and @index='3']") #登录按钮
     #用户名密码登录
    etLoginUsername=(Mb.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.EditText") #微博用户名输入框元素
    etPwd=(Mb.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View/android.widget.EditText") #微博密码输入框元素
    microblog_loginBtn=(Mb.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]") #微博密码输入框元素
    
    #手机号验证码
    et_phone=(Mb.ID,"com.ourydc.yuebaobao:id/et_phone") #微博手机号输入框元素
    et_validate_code=(Mb.ID,"com.ourydc.yuebaobao:id/patchLay") #微博验证码输入框元素
    get_validate=(Mb.ID,"com.ourydc.yuebaobao:id/tv_get_validate") #微博获取验证码按钮元素
    bindPhoneBtn=(Mb.ID,"com.ourydc.yuebaobao:id/bindPhoneBtn") #微博绑定手机号按钮元素
    refresh=(Mb.ID,"com.ourydc.yuebaobao:id/refresh") #刷新滑块儿按钮元素

