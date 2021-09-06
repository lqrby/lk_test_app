from appium.webdriver.common.mobileby import MobileBy as Mb

'''充值的页面元素'''


class RegisterPageLocators:
    # 临时的点击跳过广告
    AD = (Mb.ID, "com.asiainno.uplive:id/tvSkip")
    # 关闭广告
    close_AD = (Mb.ID, "com.asiainno.uplive:id/btnClose")
    # 我的
    click_my = (Mb.ID, "com.asiainno.uplive:id/layoutProfile")
    # 点击钱包
    click_wallet = (Mb.ID, "com.asiainno.uplive:id/txtWalletLabel")
    # 点击支付宝
    click_Alipay = (Mb.XPATH, "//*[@text='支付宝支付']")
    # 选择价格为1分钱进行购买
    click_one_minute = (Mb.XPATH, "//*[@text='0.01']")
