from appium.webdriver.common.mobileby import MobileBy as Mb

'''直播的页面元素'''


class StreamingPageLocators:
    # 点击开播按钮...
    streaming = (Mb.ID, "com.asiainno.uplive:id/ivSendLive")
    # 知道了
    roger = (Mb.ID, "com.asiainno.uplive:id/txtOk")
    #  开始直播
    Begintolive = (Mb.ID, "com.asiainno.uplive:id/btnStart")
    # 点击我知道了
    got_in = (Mb.ID, "com.asiainno.uplive:id/tvOk")
    # 视频直播
    singlelive = (Mb.XPATH, "//*[contains(@text,'视频直播')]")
    # 多人视频直播
    mutillive = (Mb.XPATH, "//*[contains(@text,'连麦交友')]")
    # 语音直播
    videolive = (Mb.XPATH, "//*[contains(@text,'声音直播')]")
    # 排麦开关
    ivMutilswitch = (Mb.ID, "com.asiainno.uplive:id/ivMutilLive")
    # 私密直播开关
    ivPrivate = (Mb.ID, "com.asiainno.uplive:id/ivPrivate")
    # 选择直播标签
    tvSelectTitle = (Mb.ID, "com.asiainno.uplive:id/tvSelectTitle")
    # 直播间更多按钮
    btnShowMore = (Mb.ID, "com.asiainno.uplive:id/btnShowMore")
    # 更多-聊天
    chat = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/tvName' and @text='聊天'")
    # 更多-分享
    share = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/tvName' and @text='分享'")
    # 更多-修改标题
    chmodtitle = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/tvName' and @text='修改标题'")
    # 更多-礼物icon
    gifticon = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/tvName' and @text='礼物'")
    # 选择礼物
    gifts = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/tvPrice' and @text<1000]")
    # 点击发送
    btnSendGift = (Mb.ID, "com.asiainno.uplive:id/btnSendGift")
    # 获取连接成功文案
    accesstocopy = (Mb.XPATH, "//*[contains(@text,'连接成功')]")
    # 点击退出直播间按钮
    quit_1 = (Mb.CLASS_NAME, "android.widget.ImageView")
    # 确定关闭直播
    certain = (Mb.ID, "android:id/button1")
    # 直播页的关闭按钮
    certain_1 = (Mb.ID, "com.asiainno.uplive:id/btnBackHome")
    # 开播授权弹窗
    allow_foreground = (Mb.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
