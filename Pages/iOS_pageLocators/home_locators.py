from appium.webdriver.common.mobileby import MobileBy as Mb
from Pages.iOS_pageLocators.hot_pageLocators import HotPageLocators


""""首页的页面元素"""
class HomePageLocator(HotPageLocators):
    # 隐私政策
    ys = (Mb.IOS_PREDICATE, 'label="我同意" and name="我同意"')
    next = (Mb.IOS_PREDICATE, 'label="确定" and name="确定"')

    # 闪屏
    flash = (Mb.IOS_PREDICATE, 'label like "*跳过"')
    # 定位权限
    location = (Mb.IOS_PREDICATE, "label == '允许' AND name == '允许' AND value == '允许'")
    SysLocation = (Mb.IOS_PREDICATE, "label == '使用App时允许'")
    # 签到
    ck = (Mb.IOS_PREDICATE, 'label == "签到"')
    # 签到窗口关闭
    ck_cl = (Mb.IOS_PREDICATE, "label == 'ck close'")
    # 去看看窗口关闭
    look_cl = (Mb.IOS_PREDICATE, "label == 'image icon close'")

    # 关闭广告
    close_AD = (Mb.IOS_PREDICATE, 'label="popup close"')

    # 首充礼包弹窗/奖励弹窗
    mall_live_close = (Mb.IOS_PREDICATE, 'label="mall live close"')

    # 青少年模式
    Adolescent = (Mb.IOS_PREDICATE, 'label="我知道了" and name="我知道了"')

    # 获取首页title
    title = (Mb.IOS_PREDICATE, 'label == "Uplive" AND name == "Uplive" AND value == "Uplive"')
    # 点击我的
    click_me = (Mb.XPATH, '//XCUIElementTypeTabBar[@name="标签栏"]/XCUIElementTypeButton[5]')
    # 点击设置
    click_set = (Mb.IOS_PREDICATE, 'label="profile icon set"')
    # 点击退出登录
    click_quit = (Mb.IOS_PREDICATE, 'label="退出登录"')
    # 点击确定退出
    click_confirm = (Mb.IOS_PREDICATE, 'label="确定"')
