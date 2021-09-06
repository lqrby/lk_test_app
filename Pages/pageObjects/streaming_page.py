import time

from Common.basepage import BasePage
from Pages.pageLocators.streaming_locators import StreamingPageLocators as loc

'''进入直播间-页面操作行为'''


class Streaming(BasePage):
    ''''''
    '''进入直播间'''

    def star_streaming(self):

        self.click_element(loc.streaming, model="点击开播按钮")
        time.sleep(1)
        # while self.is_element_exist(loc.allow_foreground[1]):
        #     self.click_element(loc.allow_foreground)
        # self.is_Begin_to_clickknow()
        #
        # self.is_got_it()
        #
        # self.is_Begintolive()

        return self

    '''获取“联系成功”文案用来做断言'''

    def success_copywriting(self):
        self.wait_eleVisible(loc.accesstocopy, model="等待页面加载-连接成功")
        return self.get_text(loc.accesstocopy, model="获取连接成功文案")

    '''开启直播时，判断是否要点击“我知道了”按钮'''

    def is_Begin_to_clickknow(self):
        try:
            if self.is_element_exist(loc.roger[1]):
                self.click_element(loc.roger, model="点击知道了")
            else:
                pass
        except:
            pass

    '''开启直播时，判断是否要点击“开始直播”按钮'''

    def is_Begintolive(self):
        try:
            if self.is_element_exist(loc.Begintolive[1], 3):
                self.click_element(loc.Begintolive, model="点击开启直播")
            else:
                pass
        except:
            pass

    '''开直播挣U转'''

    def is_got_it(self):
        try:
            if self.is_element_exist(loc.got_in[1]):
                self.click_element(loc.got_in, model="点击确定")

            else:
                pass

        except:
            pass
