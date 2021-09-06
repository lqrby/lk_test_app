from appium.webdriver.common.mobileby import MobileBy as MB


class EnvLocators:
    # 点击dokit
    dokit = (MB.IOS_PREDICATE, 'label="doraemon logo"')
    # 环境切换
    env = (MB.IOS_PREDICATE, 'name="环境切换"')
    # 线上
    disHost = (MB.IOS_PREDICATE, 'name="disHost(线上)" and label="disHost(线上)"')
    # stage
    stageHost = (MB.IOS_PREDICATE, "name='stageHost(新加坡)' and label='stageHost(新加坡)'")
    # 保存
    save = (MB.IOS_PREDICATE, 'name="保存"')
    # 返回

    # 定位权限
    location = (MB.IOS_PREDICATE, "label == '允许' AND name == '允许' AND value == '允许'")
    SysLocation = (MB.IOS_PREDICATE, "label == '使用App时允许'")
    # 签到
    ck = (MB.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton['label == '签到'']")
    # 签到窗口关闭
    ck_cl = (MB.IOS_PREDICATE, "label == 'ck close'")
    # 去看看窗口关闭
    look_cl = (MB.IOS_PREDICATE, "label == 'image icon close'")

