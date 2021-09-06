
from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy
from Pages.iOS_pageLocators.streaming_locators import StreamingLocators
from Pages.iOS_pageLocators.home_locators import HomePageLocator
import time


"""App页面公共可使用的方法"""
class CommonBus(BasePage):
    """输入文本内容，跳转至某个页面"""
    def switch_navigate(self, name):
        loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(name))
        self.wait_eleVisible(loc)
        self.click_element(loc)

    def navigate(self, id):
        loc = (MobileBy.ID, "{}".format(id))
        self.wait_eleVisible(loc)
        self.click_element(loc)

    # 开播后退出直播间
    def Get_out_of_the_studio(self):
        self.wait_eleVisible(StreamingLocators.quit_1, model="退出直播间")
        self.click_element(StreamingLocators.quit_1, model="退出直播间")

        self.wait_eleVisible(StreamingLocators.certain, model="确定退出")
        self.click_element(StreamingLocators.certain, model="确定退出")

        self.wait_eleVisible(StreamingLocators.certain, model="直播页关闭返回首页")
        self.click_element(StreamingLocators.certain, model="直播页关闭返回首页")

    # 运行完后退出App
    def quit_login(self):
        self.wait_eleVisible(HomePageLocator.click_me, model="点击我的")
        self.click_element(HomePageLocator.click_me, model="点击我的")

        self.wait_eleVisible(HomePageLocator.click_set, model="点击设置")
        self.click_element(HomePageLocator.click_set, model="点击设置")
        time.sleep(3)
        self.swipeUp()

        self.wait_eleVisible(HomePageLocator.click_quit, model="点击退出登录")
        self.click_element(HomePageLocator.click_quit, model="点击退出登录")

        self.wait_eleVisible(HomePageLocator.click_confirm, model="确定退出")
        self.click_element(HomePageLocator.click_confirm, model="确定退出")
        time.sleep(5)
        return self

