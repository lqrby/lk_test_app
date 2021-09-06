from appium.webdriver.common.mobileby import MobileBy as Mb
from TsetDatas.iOS_Datas import hotData

class HotPageLocators:
    user_name = hotData.user_name
    # 热门按钮
    hot = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar[`label == "标签栏"`]/XCUIElementTypeButton[1]')
    # 榜单
    ranking = (Mb.IOS_PREDICATE, 'label="home icon crown"')
    # 断言title
    ranking_title = (Mb.IOS_PREDICATE, 'label="Up风云榜"')
    # 返回
    arrowLeft = (Mb.IOS_PREDICATE, 'label="nav arrowLeft" and name="nav arrowLeft"')

    # 搜索
    search = (Mb.IOS_PREDICATE, 'label="home icon search" and name="home icon search"')
    # 搜索栏
    search_up = (Mb.IOS_PREDICATE, 'label="请输入用户昵称或Up号" and name="请输入用户昵称或Up号"')
    # 搜索确认
    search_ok = (Mb.IOS_PREDICATE, 'label="search" and name="search"')
    # 搜索结果断言
    search_result = (Mb.IOS_PREDICATE, 'name="' + user_name[0]['u_name'] + '"')
    # 取消
    cancel = (Mb.IOS_PREDICATE, 'label="取消" and name="取消"')

    # 消息
    message = (Mb.IOS_PREDICATE, 'label="home icon message" and name="home icon message"')
    # 消息页title断言
    message_title = (Mb.IOS_PREDICATE, 'label="消息" and name="消息"')

    # 筛选
    screen = (Mb.IOS_PREDICATE, 'label="筛选" and name="筛选"')
    # 筛选页title断言
    screen_title = (Mb.IOS_PREDICATE, 'label="筛选" and name="筛选"')
    # 台湾
    TW = (Mb.IOS_PREDICATE, 'label="台湾" and name="台湾"')
    # 台湾title
    TW_title = (Mb.IOS_PREDICATE, 'label="台湾" and name="台湾"')

    # 直播间
    room = (Mb.IOS_PREDICATE, 'label="' + user_name[0]["host_name"] + '" and' + ' name="' + user_name[0]["host_name"] + '"')
    # 聊天室连接成功
    room_text = "‎连接成功"
    room_state = (Mb.IOS_PREDICATE, 'label == "‎连接成功"')
    # 关闭直播间
    room_delete = (Mb.IOS_PREDICATE, 'label="chatRoom delete" and name="chatRoom delete"')
