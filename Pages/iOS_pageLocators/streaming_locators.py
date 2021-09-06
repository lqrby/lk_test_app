from appium.webdriver.common.mobileby import MobileBy as Mb
from Pages.iOS_pageLocators.room_locators import RoomLocators

"""直播的页面元素"""
class StreamingLocators(RoomLocators):
    # 点击开播按钮...
    streaming = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar[`label == "标签栏"`]/XCUIElementTypeButton[3]')
    # 权限
    sign = (Mb.IOS_PREDICATE, 'label == "一键开启" AND name == "一键开启" AND value == "一键开启"')
    signSys = (Mb.IOS_PREDICATE, 'label == "允许访问所有照片"')
    signNext = (Mb.IOS_PREDICATE, 'label == "好"')
    signMic = (Mb.IOS_PREDICATE, 'label == "好"')
    # 知道了
    roger = (Mb.IOS_PREDICATE, 'label == "确定" AND name == "确定" AND type == "XCUIElementTypeButton"')
    # 开始直播
    Begintolive = (Mb.IOS_PREDICATE, 'label == "开始直播" AND name == "开始直播" AND type == "XCUIElementTypeButton"')
    # 点击屏幕引导
    got_in = (Mb.IOS_PREDICATE, 'label == "右滑查看全屏"')
    # 获取连接成功文案
    text = "‎连接成功"
    accesstocopy = (Mb.IOS_PREDICATE, 'label == "连接成功"')
    # 点击退出直播间按钮
    quit_1 = (Mb.CLASS_NAME, 'label == "chatRoom delete"')
    # 确定关闭直播
    certain = (Mb.IOS_PREDICATE, 'label == "确认"')
    # 直播结束页关闭按钮
    certain_1 = (Mb.IOS_PREDICATE, 'label == "live end close"')

    # 直播结束页截图分享
    fx = (Mb.IOS_PREDICATE, 'name == "截屏分享"')
    # 奖励弹窗
    pop = (Mb.IOS_PREDICATE, 'label == "mall live close"')

    # 更多
    room_pop = (Mb.IOS_PREDICATE, 'label == "live icon pop"')
    # 聊天
    chat = (0.12, 0.64)
    # 直播分享
    share = (0.37, 0.64)
