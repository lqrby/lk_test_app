'''
@File    :  my_locators.py    
@Contact :  fangfang.song@asiainnovations.com

@Modify Time    2021/4/1 9:29 下午    
@Author  :  songfang  
@Version :  1.0
@Desciption : 
'''

from appium.webdriver.common.mobileby import MobileBy as Mb


class MyLocators:

    #=================退出登录===========
    meBtn=(Mb.ID,'com.ourydc.yuebaobao:id/iv_tab_mine') # 我的按钮
    # meBtn=(By.XPATH,'//*[@class="android.widget.RelativeLayout" and @index="4"]') # 我的按钮
    setUpBtn=(Mb.ID,'com.ourydc.yuebaobao:id/v_setting') # 设置按钮
    logoutBtn=(Mb.ID,'com.ourydc.yuebaobao:id/btn_logo_out') # 退出登录按钮
    logoutOkBtn=(Mb.ID,'com.ourydc.yuebaobao:id/tv_cancel') # 确认退出

    #     点击我的
    click_my = (Mb.ID, "com.asiainno.uplive:id/layoutProfile")
    # 点击返回
    goback = (Mb.CLASS_NAME, "android.widget.ImageButton")
    # 个人资料页返回
    back = (Mb.ID, "com.asiainno.uplive:id/back")
    # 官方客服返回
    CSback = (Mb.ID, "com.asiainno.uplive:id/chatBack")
    # 页面title
    toolbar_title = (Mb.ID, "com.asiainno.uplive:id/toolbar_title")
    # 用户昵称
    layoutName = (Mb.ID, "com.asiainno.uplive:id/layoutName")
    # 点击头像
    sdVipCover = (Mb.ID, "com.asiainno.uplive:id/ivProfilePhoto")
    # 点击编辑页
    edit = (Mb.ID, "com.asiainno.uplive:id/ivMore")
    # 点击个人资料页
    layoutGradeProgress = (Mb.ID, "com.asiainno.uplive:id/layoutGradeProgress")
    # 点击钱包
    txtWalletLabel = (Mb.ID, "com.asiainno.uplive:id/txtWalletLabel")
    # 点击任务中心
    layoutTaskCenter = (Mb.ID, "com.asiainno.uplive:id/layoutTaskCenter")
    # 点击我的庄园
    rlManor = (Mb.ID, "com.asiainno.uplive:id/rlManor")
    # 点击我的消息
    layoutProfileIM = (Mb.ID, "com.asiainno.uplive:id/layoutProfileIM")
    # 消息title
    messagetitle = (Mb.XPATH, "//*[@text='消息' and @resource-id='com.asiainno.uplive:id/title']")
    # 点击背包
    layoutProfileBag = (Mb.ID, "com.asiainno.uplive:id/layoutProfileBag")
    # 点击商城
    layoutProfileFerrari = (Mb.ID, "com.asiainno.uplive:id/layoutProfileFerrari")
    # 点击自动回复
    layoutProfileAutoResponse = (Mb.ID, "com.asiainno.uplive:id/layoutProfileAutoResponse")
    # 点击U币贡献榜
    layoutProfileContribution = (Mb.ID, "com.asiainno.uplive:id/layoutProfileContribution")
    # 点击我的家族
    layoutProfileFamilyMine = (Mb.ID, "com.asiainno.uplive:id/layoutProfileFamilyMine")
    # 家族title
    familytitle = (Mb.XPATH, "//*[@text='家族排行榜']")
    # 点击真爱团
    layoutProfileFansGroup = (Mb.ID, "com.asiainno.uplive:id/layoutProfileFansGroup")
    # 真爱团title
    fanstitle = (Mb.XPATH, "//*[@text='加入的团']")
    # 点击谁看过我
    layoutProfileFootPrint = (Mb.ID, "com.asiainno.uplive:id/layoutProfileFootPrint")
    # 点击尊享会员
    layoutProfileMember = (Mb.ID, "com.asiainno.uplive:id/layoutProfileMember")
    # 点击我的直播
    layoutProfileLive = (Mb.ID, "com.asiainno.uplive:id/layoutProfileLive")
    # 点击我的等级
    layoutProfileGrade = (Mb.ID, "com.asiainno.uplive:id/layoutProfileGrade")
    # 点击我的守护
    layoutProfileGuardian = (Mb.ID, "com.asiainno.uplive:id/layoutProfileGuardian")
    # 点击vip特权
    layoutProfileVIPGrade = (Mb.ID, "com.asiainno.uplive:id/layoutProfileVIPGrade")
    # 点击荣耀挑战赛
    layoutPkHistory = (Mb.ID, "com.asiainno.uplive:id/layoutPkHistory")
    # 荣耀战力榜title
    pktitle = (Mb.XPATH, "//*[@text='荣耀战力榜']")
    # 点击我看过的
    layoutWatchHistory = (Mb.ID, "com.asiainno.uplive:id/layoutWatchHistory")
    # 点击官方客服
    feedbackRL = (Mb.ID, "com.asiainno.uplive:id/feedbackRL")
    # 官方客服返回
    chatBack = (Mb.ID, "com.asiainno.uplive:id/chatBack")
    # 点击帮助中心
    layoutHelpCenter = (Mb.ID, "com.asiainno.uplive:id/layoutHelpCenter")
    # 点击联系我们
    layoutContactUs = (Mb.ID, "com.asiainno.uplive:id/layoutContactUs")
