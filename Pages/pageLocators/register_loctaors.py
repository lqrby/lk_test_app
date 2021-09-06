from appium.webdriver.common.mobileby import MobileBy as Mb

'''注册的页面元素'''


class RegisterPageLocators:
    # 点击登录...
    about_log = (Mb.ID, "com.asiainno.uplive:id/ivLoginType3")
    # 点击手机号登录
    phone = (Mb.XPATH, "//*[contains(@text,'手机号')]")
    # 选择国家、地区
    select_countries = (Mb.ID, "com.asiainno.uplive:id/txtCountryName")
    # 输入国家
    input_countries = (Mb.ID, "com.asiainno.uplive:id/searchTxtId")
    # 点击中国内地
    clice_China = (Mb.ID, "com.asiainno.uplive:id/sectionBodyRL")
    # 输入手机号
    phone_loc = (Mb.ID, "com.asiainno.uplive:id/editMobile")
    #   点击确定按钮
    clice_next = (Mb.ID, "com.asiainno.uplive:id/btnConfirm")
    # 输入验证码
    security_code = (Mb.ID, "com.asiainno.uplive:id/editVerifyCode")
    #    输入密码
    passaw_loc = (Mb.ID, "com.asiainno.uplive:id/textPassword")
    #     点击确定
    clice_next_1 = (Mb.ID, "com.asiainno.uplive:id/btnConfirm")
    # 个人资料-点击跳过
    click_skip = (Mb.ID, "com.asiainno.uplive:id/txtSkip")
    # 进入直播间点击退出按钮
    exit_button = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/llClose']/android.widget.ImageView[1]")
    # 退出直播间点击关闭按钮

    # 点击跳过
    skip = (Mb.ID, "com.asiainno.uplive:id/txtJump")
    # 关闭广告按钮
    close_AD = (Mb.ID, "com.asiainno.uplive:id/ivClose")
    # 游戏弹框
    closeGameInvit = (Mb.ID, "com.asiainno.uplive:id/btnClose")
    # 游客模式的登录气泡按钮
    loginPop = (Mb.ID, "com.asiainno.uplive:id/txtLogin")
    # 登录另一个账号按钮
    loginAnother = (Mb.ID, "com.asiainno.uplive:id/txtLoginAnother")
    # 选择登录方式页面标识
    chooseLogin =(Mb.ID, "com.asiainno.uplive:id/txtMore")
    # 点击我的
    click_me = (Mb.ID, "com.asiainno.uplive:id/btnProfile")
    # 点击设置
    click_set = (Mb.ID, "com.asiainno.uplive:id/layoutProfileSettings")
    # 退出登录按钮
    logout = (Mb.ID, "com.asiainno.uplive:id/logout")
    # 确认退出登录
    allowlogout = (Mb.XPATH, "//*[contains(@text,'确认')]")