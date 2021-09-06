from appium.webdriver.common.mobileby import MobileBy as Mb
from Pages.iOS_pageLocators.hot_pageLocators import HotPageLocators
from TsetDatas.iOS_Datas import roomData


class RoomLocators(HotPageLocators):
    user_name = roomData.user_name
    # 聊天
    room_chat = (Mb.IOS_PREDICATE, 'label == "live icon chat"')
    # 聊天输入框
    room_chat_in = (Mb.IOS_CLASS_CHAIN, '//*[@label=""]')
    # 发送按钮
    room_chat_send = (Mb.IOS_PREDICATE, 'label == "发送" AND name == "发送" AND type == "XCUIElementTypeButton"')
    # 验证发送内容
    room_chat_text = ()

    # 礼物
    room_gift = (Mb.IOS_PREDICATE, 'label == "live icon gift"')
    room_gift_list = (Mb.XPATH, '//ScrollView/Other[1]')
    room_gift_send = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "10"`]')

    # 分享
    room_share = (Mb.IOS_PREDICATE, 'label == "live icon share"')
    room_share_friend = (Mb.IOS_PREDICATE, 'label == "好友"')
    room_share_in = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "昵称或Up号"`]')
    room_share_who = (Mb.IOS_PREDICATE, 'label == "' + user_name[0]["u_name"]+'"')
    room_share_next = (Mb.IOS_PREDICATE, 'label == "确定"')
    share_friend_ck = 'name="发送成功"'
    room_share_wechat = (Mb.IOS_PREDICATE, 'label == "微信"')
    share_wechat_title = (Mb.IOS_PREDICATE, 'name == "选择一个聊天" AND type == "XCUIElementTypeNavigationBar"')
    share_wechat_close = (Mb.IOS_PREDICATE, 'label == "关闭" AND name == "关闭" AND type == "XCUIElementTypeButton"')
    share_wechat_ck = "分享成功"

    # 私信
    room_message = (Mb.IOS_PREDICATE, 'label == "chatroomicon message"')

    # 更多
    room_pop = (Mb.IOS_PREDICATE, 'label == "live icon pop"')
    room_pop_msg = (Mb.IOS_PREDICATE, 'label == "私信"')
    room_pop_share = (Mb.IOS_PREDICATE, 'label == "分享红包"')
    room_pop_mix = (Mb.IOS_PREDICATE, 'label == "最小化"')

    # 连麦
    room_mic = (Mb.IOS_PREDICATE, 'label == "申请连麦" AND name == "申请连麦" AND value == "申请连麦"')
    room_mic_wait = (Mb.IOS_PREDICATE, 'label == "排队中..." AND name == "排队中..." AND value == "1"')
    room_mic_close = (Mb.IOS_PREDICATE, 'label == "放弃连麦" AND name == "放弃连麦" AND value == "放弃连麦"')
    mic_close_next = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "放弃连麦"`][2]')
    mic_close_ck = "已取消连麦申请"

    # pop
    room_pop_send = (Mb.IOS_PREDICATE, 'label == "给主播赠送礼物吧，鼓励一下TA"')
