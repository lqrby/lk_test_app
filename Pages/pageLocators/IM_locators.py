from appium.webdriver.common.mobileby import MobileBy as Mb

'''IM页面元素'''


class IMPageLocator:
    # 我的
    click_my = (Mb.ID, "com.asiainno.uplive:id/layoutProfile")
    # 我的消息
    myMassage = (Mb.ID, "com.asiainno.uplive:id/layoutProfileIM")
    # 返回
    goBack = (Mb.ID, "com.asiainno.uplive:id/chatBack")
    # 收到招呼的返回
    goBack_1=(Mb.CLASS_NAME,"android.widget.ImageButton")
    '''-----------------------------官方客服页面元素-----------------------------------------------------'''

    # 官方客服
    officialCS = (Mb.XPATH, "//*[contains(@text,'官方客服')]")
    # 官方客服断言文本
    officialCS_text = (Mb.XPATH, "//*[contains(@text,'官方客服')]")

    '''-----------------------------官方助手页面元素-----------------------------------------------------'''

    # 官方助手
    officialHelper = (Mb.XPATH, "//*[contains(@text,'官方助手')]")
    # 官方助手断言title
    officialHelper_title = (Mb.XPATH, "//*[contains(@text,'官方助手')]")
    '''-----------------------------官方助手页面元素-----------------------------------------------------'''

    # 礼物助手
    giftHelper = (Mb.XPATH, "//*[contains(@text,'礼物助手')]")
    # 礼物助手断言title
    giftHelper_title = (Mb.XPATH, "//*[contains(@text,'礼物助手')]")
    '''-----------------------------打招呼页面元素-----------------------------------------------------'''

    # 打招呼
    greet = (Mb.XPATH,"//*[contains(@text,'打招呼')]")
    # 打招呼断言title
    greet_title = (Mb.XPATH, "//*[contains(@text,'收到的招呼')]")
    '''-----------------------------通讯录面元素-----------------------------------------------------'''

    # 通讯录
    contacts = (Mb.ID, "com.asiainno.uplive:id/btnContacts")
    # 输入框
    etinput = (Mb.ID, "com.asiainno.uplive:id/etInput")
    # 发送
    send = (Mb.ID, "com.asiainno.uplive:id/btnSend")
    # 获取成功的文本
    Successful_text=(Mb.XPATH,"//*[@text='这是一条pytest执行时发送的单聊内容']")

    # 互动消息
    interactMessage = (Mb.XPATH, "//*[@text='互动消息']")
    # 好友申请
    friendRequest = (Mb.XPATH, "//*[@text='好友申请']")
    # 动态通知
    dynamicNoti = (Mb.XPATH, "//*[@text='动态通知']")
    '''-----------------------------通讯录设置页面元素-----------------------------------------------------'''

    # 群聊
    group = (Mb.XPATH, "//*[@text='群聊']")
