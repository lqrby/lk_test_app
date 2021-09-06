from appium.webdriver.common.mobileby import MobileBy as Mb

'''赠送的页面元素'''


class RewardPageLocator:
    # 页面点击搜索
    search = (Mb.ID, "com.asiainno.uplive:id/ivMainInformation")
    # 查看up号
    input_up = (Mb.ID, "com.asiainno.uplive:id/editSearch")
    # 点击搜索
    click_search = (Mb.ID, "com.asiainno.uplive:id/search")
    # 点击主页
    click_list = (Mb.CLASS_NAME, "android.widget.RelativeLayout")
    # 点击进入直播间
    click_live = (Mb.ID, "com.asiainno.uplive:id/txtProfileLiveFlag")
    # 点击主播头像
    hostavatar =  (Mb.ID, "com.asiainno.uplive:id/sdTopAvatar")
    # 守护头像
    guardianavatar = (Mb.ID, "com.asiainno.uplive:id/guardianAvatar")
    # 主播昵称
    hostname = (Mb.ID, "com.asiainno.uplive:id/tvName")
    # 守护页面title
    toolbar_title = (Mb.ID, "com.asiainno.uplive:id/toolbar_title")
    # 主播贡献榜
    tvUCoins = (Mb.ID, "com.asiainno.uplive:id/tvUCoins")
    # 主播贡献榜title
    ucoinstitle = (Mb.XPATH, "//*[contains(@text,'月榜奖励')]")
    # 观众列表
    liveTopAudienceIv = (Mb.ID, "com.asiainno.uplive:id/liveTopAudienceIv")
    # 观众列表title
    guest = (Mb.XPATH, "//*[contains(@text,'贵宾')]")
    # 主播真爱团
    groupname = (Mb.ID, "com.asiainno.uplive:id/groupName")
    # 真爱团title
    grouptitle = (Mb.XPATH, "[@text='加入真爱团']")
    # 聊天按钮
    btnChat = (Mb.ID, "com.asiainno.uplive:id/btnChat")
    # 聊天框
    etInput = (Mb.ID, "com.asiainno.uplive:id/etInput")
    # 发送按钮
    btnSend = (Mb.ID, "com.asiainno.uplive:id/btnSend")
    # 点击profile弹窗头像
    sdvAvatar = (Mb.ID, "com.asiainno.uplive:id/sdvAvatar")
    # 点击关注按钮
    focus = (Mb.ID, "com.asiainno.uplive:id/layoutProfileFocus")
    # 关注按钮文本
    txtProfileFocus = (Mb.ID, "com.asiainno.uplive:id/txtProfileFocus")
    # 点击分享直播间气泡
    click_Bubble = (Mb.XPATH, "//*[contains(@text,'分享')]")
    #    点击礼物
    # vivo x50 pro 定位方式 //*[@resource-id='com.asiainno.uplive:id/llBtns']/android.view.ViewGroup[1]
   # oppo r11定位方式 click_gift = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/llBtns']/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
    click_gift = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/llBtns']/android.view.ViewGroup[1]")
    #     选择礼物
    gifts = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/tvPrice' and @text<1000]")
    # 选择礼物数量按钮
    llGiftNums = (Mb.ID, "com.asiainno.uplive:id/llGiftNums")
    # 选择礼物数量
    tvNum = (Mb.XPATH, "//*[@resource-id='com.asiainno.uplive:id/tvNum' and @text='10']")
    # 连发礼物
    tvLianfa = (Mb.ID, "com.asiainno.uplive:id/tvLianfa")
    #     点击赠送
    click_give = (Mb.ID, "com.asiainno.uplive:id/btnSendGift")
    # 赠送成功，获取文本
    get_text = (Mb.XPATH, "//*[contains(@text,'赠送了')]")
    # 直播间分享并抽奖和提示充值气泡
    popup_bubble = (Mb.ID, "com.asiainno.uplive:id/popup_bubble")