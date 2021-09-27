import re
import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from Common.log import get_logger
from Pages.pageLocators.pop_locators import PopUpLocator
from selenium.common.exceptions import NoSuchElementException, TimeoutException

log = get_logger(logger_name="基础类")
from Common import splicing
import time
import os


class BasePage:
    def __init__(self, driver):

        self.driver = driver
        

    # 等待元素可见
    def wait_eleVisible(self, loc, timeout=8, poll_frequency=0.5, model="basepage", times=2):
        """
        :param loc: 元素定位表达。元组类型，表达方式(元素定位类型，元素定位方法)
        :param timeout: 等待上限。
        :param poll_frequency: 轮询频率
        :param model: 等待失败时，截图操作，图片文件中需要表达的功能模块标注。
        :return: None
        """
        log.info("{1}: 等待元素可见 {0}".format(loc, model))
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            if times > 0:
                times -= 1
                if self.pop(PopUpLocator.popList):
                    self.wait_eleVisible(loc, model=model, times=times)
                else:
                    self.save_webImgs(model)
                    log.exception("等待元素可见失败。")
                    log.info(e)
             
            else:
                self.save_webImgs(model)
                log.exception("等待元素可见失败。")
                log.info(e)
            

        else:
            pass
    
    #元素是否显示
    def is_desplayed(self, loc, model=None):
        # log.info("{0}:list元素 {1}".format(model, loc))
        try:
            return self.driver.find_elements(*loc)
        except:
            log.exception("元素不存在===={}".format(loc))
            # 截图
            self.save_webImgs(model)
            raise

    # 等待某个元素可以被点击，不可点击则截图
    def wait_element_clickable(self, loc, timeout=8, poll_frequency=0.5, model="等待可点击截图", times=1):
        log.info("等待元素可点击:{}".format(loc))
        try:
            el = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(loc))
            return el
        except:
            if times > 0:
                times -= 1
                if self.pop(PopUpLocator.popList):
                    self.wait_element_presence(loc, model=model, times=times)
                else:
                    log.error("未找到或元素不可点击{}".format(loc))
                    self.save_webImgs(model)
            else:
                log.error("未找到或元素不可点击{}".format(loc))
                self.save_webImgs(model)
            

    

    # 某个元素存在
    def wait_element_presence(self, loc, timeout=8, poll_frequency=0.5, model=None, times=1):
        log.info("元素是否存在:{}".format(loc))
        try:
            el = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(loc)
            )
            return el
        except:
            if times > 0:
                times -= 1
                if self.pop(PopUpLocator.popList):
                    self.wait_element_presence(loc, model=model, times=times)
            else:
                self.save_webImgs(model)
                log.error("元素不存在:{}".format(loc))

    # 查找一个元素
    def get_element(self, loc, model="basepage"):
        log.info("{0}：获取元素 {1}".format(model, loc))
        try:
            return self.driver.find_element(*loc)
        except:
            log.exception("获取元素失败:{}".format(loc))
            # 截图
            self.save_webImgs(model)
            raise

    # 查找一个元素
    def find_element(self, loc):
        return self.driver.find_element(*loc)

    # 查找相同的元素
    def find_elements(self, loc):
        return self.driver.find_elements(*loc)
        

    def get_elements(self, loc):
        try:
            return self.driver.find_elements(*loc)
        except:
            log.exception("定位元素失败")
            self.save_webImgs()
            raise

    # 输入操作
    def input_text(self, loc, text, model=None):
        # 查找元素
        ele = self.get_element(loc)
        # 输入操作
        log.info("{0}: 在元素 {1} 中输入文本：{2}".format(model, loc, text))
        try:
            ele.send_keys(text)
        except:
            log.exception("输入操作失败")
            # 截图
            self.save_webImgs(model)
            raise

    # 清除操作
    def clear_input_text(self, loc, model=None):
        # 找元素再清除
        ele = self.get_element(loc, model)
        # 点击操作
        log.info("{0}: 元素：{1} 清除文本内容。".format(model, loc))
        try:
            ele.clear()
        except:
            # 捕获异常到日志中；
            log.exception("元素：{0} 清除文本内容失败。：".format(loc))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 点击操作
    def click_element(self, loc, model=None, times=3):
        time.sleep(1)
        if self.is_desplayed(loc) and EC.element_to_be_clickable(loc):
            # 找到元素
            ele = self.get_element(loc, model)
            try:
                ele.click()
            except:
                # 捕获异常到日志中；
                log.exception("点击元素:{0} 点击事件失败:".format(loc))
                # 截图 - 保存到的指定的目录。名字要想好怎么取？
                self.save_webImgs(model)
                # 抛出异常
                raise
        else:
            if times > 0:
                # PopThread(self.driver, PopUp.popList)
                times -= 1
                item = self.pop(PopUpLocator.popList)
                if item == PopUpLocator.close_broadcast:
                    log.info("=========聊天室已关闭==========")
                    self.driver.close_app()
                    self.driver.quit()
                if item:
                    self.click_element(loc, model=model, times=times)
                else:
                    # 捕获异常到日志中；
                    log.exception("点击元素:{0} 点击事件失败:".format(loc))
                    # 截图 - 保存到的指定的目录。名字要想好怎么取？
                    self.save_webImgs(model)
            else:
                pass

    
    # 判断元素是否可点击
    def is_clickable(self, loc):
        if self.is_element_exist(loc) and EC.element_to_be_clickable(loc):
            return True
        else:
            return False

    # 点击操作
    def click_element_byele(self, ele, model=None):
        # 点击操作
        log.info("{0}: 元素：{1} 点击事件。".format(model, ele))
        try:
            ele.click()
        except:
            # 捕获异常到日志中；
            log.exception("元素：{0} 点击事件失败：".format(ele))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 获取文本内容
    def get_text(self, loc, model=None):
        # 找到元素
        ele = self.get_element(loc, model)
        # 获取元素的文本内容
        log.info("{0}：获取元素：{1} 的文本内容".format(model, loc))
        try:
            text = ele.text
            log.info("{0}：元素：{1} 的文本内容为：{2}".format(model, loc, text))
            return text
        except:
            # 捕获异常到日志中；
            log.exception("获取元素：{0} 的文本内容失败。报错信息如下：".format(loc))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 获取元素的属性
    def get_element_attribute(self, loc, attr_name, model=None):
        # 找到元素
        ele = self.get_element(loc, model)
        # 获取元素的属性
        log.info("{0}: 获取元素：{1} 的属性：{2}".format(model, loc, attr_name))
        try:
            value = ele.get_attribute(attr_name)
            log.info("{0}: 元素：{1} 的属性：{2} 值为：{3}".format(model, loc, attr_name, value))
            return value
        except:
            # 捕获异常到日志中；
            log.exception("获取元素：{0} 的属性：{1} 失败，异常信息如下：".format(loc, attr_name))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 截图
    def save_webImgs(self, model=None):
        # 写的实时时间戳
        now = time.strftime("%Y-%m-%d-%H-%M-%S")
        # 图片的名称和时间戳
        filePath = "{}_{}.png".format(now,model)
        # 截图保存的路径：截图文件存放在 screenshot目录下
        img_path = os.path.join(splicing.screenshot_dir, filePath)
        try:
            self.driver.save_screenshot(img_path)
            allure.attach(self.driver.get_screenshot_as_png(), model, allure.attachment_type.PNG)
        except:
            log.exception("截图失败")
        else:
            log.info("截屏成功。图片路径为{0}".format(img_path))

    # webview切换
    def switch_webview(self, webview_name, timeout=30, poll_frequency=0.5, model=None):
        # 等待webview元素出现
        loc = (MobileBy.CLASS_NAME, "android..webview")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((loc)))
        # 获取所有的上下文  列表
        contexts = self.driver.contexts
        # 判断你webview 名称  是否  在当前的上下文当中，如果 在就切换，如果不在就报错。
        if webview_name in contexts:
            # 切换
            self.driver.switch_to.context(webview_name)
        else:
            # 抛出异常。
            pass

    #
    # 进入webview后，使用Uc-devtools开发者调试工具，下载驱动器对应webview版本的
    # 获取设备的大小
    # 获取元素的大小、坐标

    # 使用坐标点击
    def tap_by_coordinate(self, size, times=1, model=None):
        window = self.driver.get_window_size()
        x = window["width"] * size[0]
        y = window["height"] * size[1]

        try:
            TouchAction(self.driver).tap(x=x, y=y, count=times).perform()
        except:
            log.exception("等待元素可见失败。")
            # 截图
            self.save_webImgs(model)
            raise

    # 滑屏操作 - 向上滑屏
    def swipeUp(self, t=500, n=1):
        time.sleep(0.5)
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
            time.sleep(0.5)



    def get_size(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return x, y


    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        time.sleep(0.5)
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.25
        y2 = l['height'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        time.sleep(0.5)
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.8
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.2
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipeRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        time.sleep(0.5)
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.20
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.8
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # 滑屏操作-左右滑屏 有bug
    # def swipe_lef_right(self, start_y_percent=0.9, end_y_percent=0.1):
    #     size = self.get_device_size()
    #     self.driver.swipe(size["widht"] * start_y_percent, size["height"] * 0.5, size["widht"] * end_y_percent)
    #     time.sleep(0.5)

    # 滑屏操作-左右滑屏输入开始和结束0-1之间
    def swipe_lef_right(self, start_x, end_x):
        size = self.driver.get_window_size()
        x1 = int(size["width"] * start_x)
        y1 = int(size["height"] * 0.5)
        x2 = int(size["width"] * end_x)
        # print(x1, x2)
        self.driver.swipe(x1, y1, x2, y1, 500)
        time.sleep(1)

    #向右拖动   
    def drag_right(self):
        TouchAction(self.driver).press(x=258,y=1212).wait(2000).move_to(x=700,y=1212).wait(1000).release().perform()
        

    # iOS滑屏操作
    def is_swipe(self, start_x, start_y, end_x, end_y):
        time.sleep(5)
        size = self.driver.get_window_size()
        x1 = int(size["width"] * start_x)
        y1 = int(size["height"] * start_y)
        x2 = int(size["width"] * end_x)
        y2 = int(size["height"] * end_y)
        # print(x1, x2)
        self.driver.swipe(x1, y1, x2, y2, 500)
        time.sleep(2)

    # 直播间聊天室滑动至元素可见
    def swipeToView(self, text):
        try:
            WebDriverWait(self.driver, 15, 0.5).until(EC.visibility_of_element_located((MobileBy.IOS_PREDICATE, text)))
        except:
            while text not in self.driver.page_source:
                self.is_swipe(0.2, 0.8, 0.2, 1)
                time.sleep(1)

    # iOS左右滑动元素 使用js，direction：lef or right，element是定位
    def swipe_element(self, direction, element):
        try:
            self.driver.execute_script("mobile:swipe", {"direction": direction, 'element': element, "duration": 1})
        except:
            raise

    # 使用js定位到的元素拖动到可见区域
    def scrollToElement(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # iOS toast获取
    def isToastMessage(self, message):
        try:
            ele = WebDriverWait(self.driver, 20, 0.1).until(
                EC.presence_of_element_located((MobileBy.IOS_PREDICATE, message)))
            log.info("查找到toast----%s" % message)
            return ele.text
        except:
            log.error("未查找到toast----%s" % message)
            return False

    # toast获取
    def get_toast_msg(self, part_text, model=None):
        # xpath表达式
        xpath_loc = '//*[contains(@text,"{}")]'.format(part_text)
        log.info("{0}: 获取toast信息，表达式为：{1}".format(model, xpath_loc))
        try:
            # 等待元素存在
            WebDriverWait(self.driver, 5, 0.03).until(EC.presence_of_element_located((MobileBy.XPATH, xpath_loc)))
            return self.get_element((MobileBy.XPATH, xpath_loc)).text
        except:
            # 抛异常
            log.exception("获取toast失败")
            self.save_webImgs(model)
            raise

    

    def get_toast_exist(self,message):
        xpath_loc = '//*[contains(@text,"{}")]'.format(message)
        try:
            WebDriverWait(self.driver, 8, 0.02).until(EC.presence_of_element_located((MobileBy.XPATH, xpath_loc)))
            return self.get_element((MobileBy.XPATH, xpath_loc)).text
        except:
            return "获取toast失败"

    # 列表滑动操作-翻页找其他页面的内容
    def scrollListView(self, text):
        try:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(text))
            
        except:
            self.swipeUp()
            time.sleep(0.5)
            self.scrollListView(text)

    # iOS滑动操作-翻页找其他页面的内容
    def scrollToView(self, loc):
        try:
            WebDriverWait(self.driver, 15, 0.5).until(EC.visibility_of_element_located(loc))
        except:
            s = loc[1].split("name=")[1]
            while s in self.driver.page_source:
                self.swipeUp()
                time.sleep(0.5)
                if WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(loc)):
                    break

    # 获取设备大小
    def get_device_size(self):
        try:
            return self.driver.get_window_size()
        except:
            pass

    # 消除气泡后点击
    def unbubble(self, loc):
        waittime = 0
        while waittime < 5:
            flag = self.is_desplayed(loc)
            if flag:
                pass
            else:
                self.tap_by_coordinate((0.5, 0.4))
                waittime += 1
                time.sleep(1)
            return False


    # 判断元素是否存在
    def is_element_exist(self, element):
        try:
            self.find_element(element)
        except NoSuchElementException:
            return False
        else:
            return True

    # 元素存在就点击否则pass
    def exist_be_click(self, element, model=None):
        try:
            WebDriverWait(self.driver, 2, 0.2).until(EC.presence_of_element_located(element))
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass
        else:
            self.click_element(element,model=model)

    # 元素是否存在-iOS
    def element_exist(self, elementName):
        source = self.driver.page_source
        result = re.search('label="' + elementName + '" enabled="true"', source)
        if result is not None:
            return True
        else:
            return False

    def page(self, name):
        '''
        返回至指定页面
        :return:
        '''
        i = 0
        while i < 10:
            i = i + 1
            try:
                findname = "//*[@text='%s']" % (name)
                self.driver.find_element_by_xpath(findname)
                self.driver.implicitly_wait(2)
                break
            except:
                os.popen("adb shell input keyevent 4")
                try:
                    self.driver.find_element_by_xpath("//*[@text='首页']")
                    self.driver.implicitly_wait(2)
                    break
                except:
                    os.popen("adb shell input keyevent 4")

    
    # def pop(self, pop_list):
    #     try:
    #         time.sleep(2)
    #         # source = self.driver.page_source
    #         # # print(source)
    #         for i in pop_list:
    #             log.info("循环查找pop")
    #             if i in source:
    #                 pop = SignPopPage(self.driver, i)
    #                 pop.close_ivClose().closeGameInvit().skipAD().systempop().locatpop().privacy().test_ad(). \
    #                     check_bounced().is_Begintolive().close_language().Adolescent_model()
    #     except Exception as e:
    #         print(e)


    def pop(self, pop_list):
        time.sleep(2)
        source = self.driver.page_source
        mark = ""
        for i in pop_list:
            log.info("循环检测页面是否有弹窗元素:{}".format(i))
            if i[1] in source:
                self.click_element(i)
                mark = i
                break
        return mark
