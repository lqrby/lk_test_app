from appium.webdriver.common.mobileby import MobileBy as Mb
from TsetDatas.iOS_Datas import profileData


class ProfilePage:
    num = profileData.user_name
    # 用户up号
    up_num = (Mb.IOS_PREDICATE, 'label == "Up号："' + num['up_num'] + '"')
    # 分享
    share = (Mb.IOS_PREDICATE, 'label == "profile icon share white"')
    # 更多
    more = (Mb.IOS_PREDICATE, 'abel == "im icon more2"')
    # 私信
    msn = (Mb.IOS_PREDICATE, 'label == "私信"')

