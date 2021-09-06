from appium.webdriver.common.mobileby import MobileBy as Mb

'''首页的页面元素'''


class HotPageLocator:
    '''热门主页面元素'''
    # 热门title
    title = (Mb.XPATH, "//*[@text='Uplive']")
    # 排行榜
    ivRank = (Mb.ID, "com.asiainno.uplive:id/ivRank")
    # 搜索
    ivMainInformation = (Mb.ID, "com.asiainno.uplive:id/ivMainInformation")
    # 聊天
    ivIM = (Mb.ID, "com.asiainno.uplive:id/ivIM")
    # 筛选
    layoutMore = (Mb.ID, "com.asiainno.uplive:id/layoutMore")
    # 显示所有标签
    ivShowAllLabel = (Mb.ID, "com.asiainno.uplive:id/ivShowAllLabel")
    # 排行榜页面title
    rankTitle = (Mb.ID, "com.asiainno.uplive:id/toolbar_title")
    # 选择大区排行榜
    btnSelectRank = (Mb.ID, "com.asiainno.uplive:id/btnSelectRank")
    # 搜索框
    editSearch = (Mb.ID, "com.asiainno.uplive:id/editSearch")
    # 搜索按钮
    search = (Mb.ID, "com.asiainno.uplive:id/search")
    # IM页面title
    IMtitle = (Mb.ID, "com.asiainno.uplive:id/title")
    # 筛选页面title
    toolbar_title = (Mb.ID, "com.asiainno.uplive:id/toolbar_title")
    # 选择标签title
    tvTitle = (Mb.ID, "com.asiainno.uplive:id/tvTitle")
    # 返回按钮
    back = (Mb.XPATH, "//android.widget.ImageButton")
    # 消息返回
    messageback = (Mb.ID, "com.asiainno.uplive:id/back")
    # 进入热门直播间
    hotroom = (Mb.ID, "//*[@resource-id='com.asiainno.uplive:id/ivLiveImageBorder']")

    '''排行榜页面元素'''
    # 主播月榜
    hostrank = (Mb.XPATH, "//androidx.appcompat.app.ActionBar.Tab[@content-desc='月榜']/android.widget.TextView")
    # 用户等级
    txtGrade = (Mb.ID, "com.asiainno.uplive:id/txtGrade")
    # 财富榜总榜
    totalrank = (Mb.XPATH, "//androidx.appcompat.app.ActionBar.Tab[@content-desc='总榜']/android.widget.TextView")
    # 礼物星榜无数据
    nostarrank = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/pagerRank3']/android.widget.FrameLayout/android"
                         ".widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView")
    # 守护总榜
    guardian = (Mb.XPATH, "//androidx.appcompat.app.ActionBar.Tab[@content-desc='总榜']/android.widget.TextView")
    # 守护总榜第一的守护是否存在
    ivGuardianPhoto = (Mb.ID, "com.asiainno.uplive:id/ivGuardianPhotoBorder")


    '''筛选页面标签'''
    country = (Mb.XPATH, "//*[@text='连麦']")
    moretitle = (Mb.ID, "com.asiainno.uplive:id/toolbar_title")

    '''标签弹窗元素'''
    # 选择连麦标签
    labelselect = (Mb.XPATH, "//*[@text='连麦']")
    # 点击确定
    lableconfirm = (Mb.ID, "com.asiainno.uplive:id/txtConfirm")
