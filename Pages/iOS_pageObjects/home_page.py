from Common.basepage import BasePage
from Pages.iOS_pageLocators.home_locators import HomePageLocator as loc
from selenium.common.exceptions import NoSuchElementException
from Common.log import get_logger
import time

log = get_logger(logger_name="首页操作日志")

'''首页-页面操作'''
class HomePage(BasePage):
    """登录成功后获取首页的title做断言"""
    '''在首页判断完成广告，获取title做断言'''
    def success_title(self):
        # 过滤弹窗
        self.Adolescent_model()
        self.AD()
        self.check_bounced()
        self.reward_pop()
        # 获取首页title
        self.wait_eleVisible(loc.title, model="获取title")
        return self.get_text(loc.title, model="获取title")

    '''注册成功后获取首页title做断言'''
    def register_title(self):
        time.sleep(3)
        self.wait_eleVisible(loc.title, model="获取title")
        return self.get_text(loc.title, model="获取title")

    '''判断首页是否有广告'''
    def AD(self):
        if self.is_desplayed(loc.close_AD):
            self.click_element(loc.close_AD, model="关闭首页广告")
        else:
            pass

    """启动闪屏"""
    def flash_skip(self):
        if self.is_desplayed(loc.flash):
            self.click_element(loc.flash, model="点击跳过")
        else:
            pass

    '''进入首页判断是否有青少年模式'''
    def Adolescent_model(self):
        if self.is_desplayed(loc.Adolescent):
            self.click_element(loc.Adolescent, model="关闭青少年模式")
        else:
            pass

    '''进入首页判断是否有签到'''
    def check_bounced(self):
        log.info("判断页面签到按钮")
        try:
            bounced = self.get_element(loc.ck, model="判断是否有签到按钮")
        except NoSuchElementException:
            log.info("没有签到按钮")
        else:
            bounced.click()
            self.click_element(loc.ck_cl, model="点击签到弹框关闭按钮")

    # 奖励弹窗
    def reward_pop(self):
        if self.is_desplayed(loc.mall_live_close):
            self.click_element(loc.mall_live_close, model="关闭弹窗")
        else:
            pass

    def clickMy(self):
        self.wait_element_clickable(loc.click_me)
        self.click_element(loc.click_me, model="点击我的")

    # 判断是否是热门
    def hot_check(self):
        if self.is_desplayed(loc.title):
            pass
        else:
            self.click_element(loc.hot, model="点击热门")
