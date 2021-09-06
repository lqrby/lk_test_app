from appium.webdriver.common.mobileby import MobileBy as Mb

# 关注模块
class FollowPage:
    # 关注tab
    follow_tab = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "关注"`][1]')
    # 广场tab
    gc_tab = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "广场"`]')
    # 奖励
    jl_tab = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "奖励"`]')

    # 推荐主播
    # +关注
    follow_add = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "关注"`][2]')
    # 已关注
    follow = (Mb.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "已关注"`]')

    # 广场
    # 发布按钮
    send = (Mb.IOS_PREDICATE, 'label == "square icon release"')
    # 发布内容
    send_text = (Mb.IOS_PREDICATE, 'type == "XCUIElementTypeTextView"')
    # 本地图片
    send_pic = (Mb.IOS_PREDICATE, 'label == "feed public selectPic"')
    send_pic_tap = (Mb.IOS_PREDICATE, '**/XCUIElementTypeButton[`label == "photo icon check"`][1]')
    send_pic_next = (Mb.IOS_PREDICATE, 'label like "下一步*" and value like "下一步*"')
    # 本地视频
    send_video = (Mb.IOS_PREDICATE, 'label == "feed public selectVideo"')
    send_video_next = (Mb.IOS_PREDICATE, 'label like "下一步*" and value like "下一步*"')
    # 发布
    send_next = (Mb.IOS_PREDICATE, '**/XCUIElementTypeButton[`label == "发布"`]')


