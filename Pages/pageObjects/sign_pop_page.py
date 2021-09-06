"""
======================
@author：songfang
@time:2021/3/22-1:40 下午
======================
"""
from Pages.pageLocators.pop_locators import PopUp as loc


class SignPopPage():
    def __init__(self, driver, pop):
        self.pop = pop
        self.driver = driver

    """关闭邀请入房邀请"""

    def close_ivClose(self):
        if self.pop == loc.popList[0]:
            ele = self.driver.find_element(*loc.closeInvitInRoom)
            ele.click()
            # self.click_element(loc.closeInvitInRoom, model="点击关闭邀请入房邀请")
        return self

    """关闭游戏推广弹窗"""

    def closeGameInvit(self):
        if self.pop == loc.popList[1]:
            ele = self.driver.find_element(*loc.closeGameInvit)
            ele.click()
            # self.click_element(loc.closeGameInvit, model="点击关闭游戏推广弹窗")
        return self

    '''跳过开屏广告'''

    def skipAD(self):
        if self.pop == loc.popList[2]:
            ele = self.driver.find_element(*loc.skipAD)
            ele.click()
            # self.click_element(loc.skipAD, model="跳过开屏广告")
        return self

    # 系统弹窗
    def systempop(self):
        if self.pop == loc.popList[3]:
            ele = self.driver.find_element(*loc.allowpop1)
            ele.click()
            # self.click_element(loc.allowpop1, model="点击允许系统权限弹窗")
            return self
        elif self.pop == loc.popList[4]:
            ele = self.driver.find_element(*loc.allowpop2)
            ele.click()
            # self.click_element(loc.allowpop2, model="点击允许系统权限弹窗")
            return self
        elif self.pop == loc.popList[5]:
            ele = self.driver.find_element(*loc.onlyappallow)
            ele.click()
            # self.click_element(loc.onlyappallow, model="点击允许系统权限弹窗")
            return self
        else:
            return self

    # 允许定位弹窗
    def locatpop(self):
        if self.pop == loc.popList[6]:
            ele = self.driver.find_element(*loc.allowlocat)
            ele.click()
            # self.click_element(loc.allowlocat, "允许定位弹窗")
            if self.driver.find_element(*loc.onlyappallow).is_displayed():
                ele = self.driver.find_element(*loc.onlyappallow)
                ele.click()
                # self.click_element(loc.onlyappallow, model="点击允许系统权限弹窗")
        return self

    '''判断是否有隐私政策弹窗'''

    def privacy(self):
        if self.pop == loc.popList[7]:
            ele = self.driver.find_element(*loc.dialog)
            ele.click()
            ele1 = self.driver.find_element(*loc.txtOk)
            ele1.click()
            # self.click_element(loc.dialog, "点击隐私政策同意")
            # self.click_element(loc.txtOk, "点击隐私政策确定")
        return self

    '''判断首页是否有广告'''

    def test_ad(self):
        if self.pop == loc.popList[8]:
            ele = self.driver.find_element(*loc.close_AD)
            ele.click()
            # self.click_element(loc.close_AD, model="关闭首页广告")
        return self

    '''进入首页判断是否有签到'''

    def check_bounced(self):
        if self.pop == loc.popList[9]:
            ele = self.driver.find_element(*loc.check_shut)
            ele.click()
            # self.click_element(loc.check_shut, model="点击签到弹框关闭按钮")
        return self

    '''开启直播时，判断是否要点击“开始直播”按钮'''

    def is_Begintolive(self):
        if self.pop == loc.popList[10]:
            ele = self.driver.find_element(*loc.got_in)
            ele.click()
            # self.click_element(loc.got_in, model="点击开启直播")
        return self

    '''关闭热门语言偏好'''

    def close_language(self):
        if self.pop == loc.popList[11]:
            ele = self.driver.find_element(*loc.txtSkip)
            ele.click()
            # self.click_element(loc.txtSkip, model="点击跳过语言偏好设置")
        return self

    '''进入首页判断是否有青少年模式'''

    def Adolescent_model(self):
        if self.pop == loc.popList[12]:
            ele = self.driver.find_element(*loc.Adolescent)
            ele.click()
            # self.click_element(loc.Adolescent, model="关闭青少年模式")
        return self
