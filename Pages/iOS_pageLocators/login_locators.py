from appium.webdriver.common.mobileby import MobileBy as Mb

'''登录页面元素'''


class LoginPageLocator:
    # 游客模式
    guest_login = (Mb.IOS_PREDICATE, 'name="登录" and label="登录"')

    # 点击手机号登录
    phone = (Mb.IOS_PREDICATE, "name like '手机*'")
    # 选择国家、地区
    # select_countries = (Mb.XPATH, "//XCUIElementTypeStaticText[@name='国家/地区']")
    # # 输入国家
    # input_countries = (Mb.XPATH, "//XCUIElementTypeStaticText[@name='搜索']")
    # # 点击中国内地
    # clice_China = (Mb.XPATH, "//XCUIElementTypeStaticText[@name='中国内地']")
    # 输入手机号
    phone_loc = (Mb.CLASS_NAME, "XCUIElementTypeTextField[2]")
    #   点击确定按钮
    clice_next = (Mb.IOS_PREDICATE, 'label="确定" and name="确定"')
    # 随意点击
    # random_clice = (Mb.ID, "com.asiainno.uplive:id/upToolbar")
    #    输入密码
    passaw_loc = (Mb.XPATH, '//*[@label=""]')
    #     点击确定
    clice_next_pwd = (Mb.IOS_PREDICATE, 'label="确定" and name="确定"')
    # 登录成功提示
    login_text = 'name="登录成功"'

    # 微博登录

