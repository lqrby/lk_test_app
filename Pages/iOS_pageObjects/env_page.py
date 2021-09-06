from Common.basepage import BasePage
from Pages.iOS_pageLocators.env_locators import EnvLocators as loc
from selenium.common.exceptions import NoSuchElementException
from Common.log import get_logger
import time


class EnvPage(BasePage):
    # 环境切换
    def env_change(self, env):
        self.wait_eleVisible(loc.dokit, model="等待dokit")
        self.click_element(loc.dokit, model="点击dokit图标")
        self.wait_eleVisible(loc.env, model="等待环境切换")
        self.click_element(loc.env, model="点击环境切换")
        if env == "stage":
            self.wait_eleVisible(loc.stageHost, model="等待stage")
            self.click_element(loc.stageHost, model="点击stage")
        if env == "dis":
            self.wait_eleVisible(loc.disHost, model="等待disHost")
            self.click_element(loc.disHost, model="点击disHost")
        # 判断环境是否选择
        if self.element_exist("保存"):
            self.click_element(loc.save, model="点击保存")
        else:
            self.swipe_lef_right(0, 1)
            print("退出环境切换")






