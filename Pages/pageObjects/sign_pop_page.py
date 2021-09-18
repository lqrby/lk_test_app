"""
======================
@author：songfang
@time:2021/3/22-1:40 下午
======================
"""
from Pages.pageLocators.pop_locators import PopUpLocator as poploc


class SignPopPage():
    def __init__(self, driver, pop):
        self.pop = pop
        self.driver = driver

    """关闭邀请入房邀请"""

    def close_ivClose(self):
        if self.pop == poploc.popList[0]:
            ele = self.driver.find_element(*poploc.close_back)
            ele.click()
            # self.click_element(poploc.closeInvitInRoom, model="点击关闭邀请入房邀请")
        return self

    """关闭游戏推广弹窗"""

    def closeGameInvit(self):
        if self.pop == poploc.popList[1]:
            ele = self.driver.find_element(*poploc.closeGameInvit)
            ele.click()
            # self.click_element(poploc.closeGameInvit, model="点击关闭游戏推广弹窗")
        return self

    '''跳过开屏广告'''

    def skipAD(self):
        if self.pop == poploc.popList[2]:
            ele = self.driver.find_element(*poploc.skipAD)
            ele.click()
            # self.click_element(poploc.skipAD, model="跳过开屏广告")
        return self

    # 系统弹窗
    def systempop(self):
        if self.pop == poploc.popList[3]:
            ele = self.driver.find_element(*poploc.allowpop1)
            ele.click()
            # self.click_element(poploc.allowpop1, model="点击允许系统权限弹窗")
            return self
        elif self.pop == poploc.popList[4]:
            ele = self.driver.find_element(*poploc.allowpop2)
            ele.click()
            # self.click_element(poploc.allowpop2, model="点击允许系统权限弹窗")
            return self
        elif self.pop == poploc.popList[5]:
            ele = self.driver.find_element(*poploc.onlyappallow)
            ele.click()
            # self.click_element(poploc.onlyappallow, model="点击允许系统权限弹窗")
            return self
        else:
            return self

    # 允许定位弹窗
    def poplocatpop(self):
        if self.pop == poploc.popList[6]:
            ele = self.driver.find_element(*poploc.allowpoplocat)
            ele.click()
            # self.click_element(poploc.allowpoplocat, "允许定位弹窗")
            if self.driver.find_element(*poploc.onlyappallow).is_displayed():
                ele = self.driver.find_element(*poploc.onlyappallow)
                ele.click()
                # self.click_element(poploc.onlyappallow, model="点击允许系统权限弹窗")
        return self

    '''判断是否有隐私政策弹窗'''

    def privacy(self):
        if self.pop == poploc.popList[7]:
            ele = self.driver.find_element(*poploc.dialog)
            ele.click()
            ele1 = self.driver.find_element(*poploc.txtOk)
            ele1.click()
            # self.click_element(poploc.dialog, "点击隐私政策同意")
            # self.click_element(poploc.txtOk, "点击隐私政策确定")
        return self

    '''判断首页是否有广告'''

    def test_ad(self):
        if self.pop == poploc.popList[8]:
            ele = self.driver.find_element(*poploc.close_AD)
            ele.click()
            # self.click_element(poploc.close_AD, model="关闭首页广告")
        return self

    '''进入首页判断是否有签到'''

    def check_bounced(self):
        if self.pop == poploc.popList[9]:
            ele = self.driver.find_element(*poploc.check_shut)
            ele.click()
            # self.click_element(poploc.check_shut, model="点击签到弹框关闭按钮")
        return self

    '''开启直播时，判断是否要点击“开始直播”按钮'''

    def is_Begintolive(self):
        if self.pop == poploc.popList[10]:
            ele = self.driver.find_element(*poploc.got_in)
            ele.click()
            # self.click_element(poploc.got_in, model="点击开启直播")
        return self

    '''关闭热门语言偏好'''

    def close_language(self):
        if self.pop == poploc.popList[11]:
            ele = self.driver.find_element(*poploc.txtSkip)
            ele.click()
            # self.click_element(poploc.txtSkip, model="点击跳过语言偏好设置")
        return self

    '''进入首页判断是否有青少年模式'''

    def Adolescent_model(self):
        if self.pop == poploc.popList[12]:
            ele = self.driver.find_element(*poploc.Adolescent)
            ele.click()
            # self.click_element(poploc.Adolescent, model="关闭青少年模式")
        return self
