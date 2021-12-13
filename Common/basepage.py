import re, allure, time, os
from subprocess import run, PIPE
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.search_context import mobile
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from Common.log import get_logger
from Pages.pageLocators.pop_locators import PopUpLocator
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.connectiontype import ConnectionType
log = get_logger(logger_name="基础类")
from Common import splicing



class BasePage:
    def __init__(self, driver):

        self.driver = driver
        
    
    # 等待元素可见
    def wait_eleVisible(self, loc, timeout=8, poll_frequency=0.5, model="basepage"):
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
            if self.get_getWebState() == 6:
                self.wait_eleVisible(loc,timeout=timeout, poll_frequency=poll_frequency, model=model)
            if self.check_page_popUp():
                self.wait_eleVisible(loc,timeout=timeout, poll_frequency=poll_frequency, model=model)
            else:
                self.save_webImgs(model)
                # log.exception("等待元素可见失败")
                # log.info(e)
                self.exit_and_overRun()
        
    
    # 等待某个元素可以被点击，不可点击则截图
    def wait_element_clickable(self, loc, timeout=8, poll_frequency=0.5, model="等待可点击"):
        log.info("等待元素可点击:{}".format(loc))
        try:
            el = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(loc))
            return el
        except:
            if self.get_getWebState() == 6:
                self.wait_element_clickable(loc,timeout=timeout, poll_frequency=poll_frequency, model=model)
            if self.check_page_popUp():
                return self.wait_element_clickable(loc,timeout=timeout, poll_frequency=poll_frequency, model=model)
            else:
                log.error("未找到或元素不可点击{}".format(loc))
                self.save_webImgs(model)
                self.exit_and_overRun()
                return False
            

    # 某个元素存在
    def wait_element_presence(self, loc, timeout=8, poll_frequency=0.5, model=None):
        log.info("{}元素是否存在:{}".format(model,loc))
        try:
            el = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(loc)
            )
            return el
        except:
            if self.get_getWebState() == 6:
                self.wait_element_presence(loc,timeout=timeout, poll_frequency=poll_frequency, model=model)
            if self.check_page_popUp():
                return self.wait_element_presence(loc,timeout=timeout, poll_frequency=poll_frequency, model=model)
            else:
                self.save_webImgs(model)
                log.error("元素不存在:{}".format(loc))
                self.exit_and_overRun()
                return False


    # #获取当前网络状态
    # def get_getWebState(self):
    #     state=self.driver.network_connection
    #     if state == 0:
    #         log.info("无网络连接")
    #         self.save_webImgs(model="无网络连接")
    #         time.sleep(30)
    #         state=self.driver.network_connection
    #         if state != 6:
    #             self.exit_and_overRun() 
    #         else:
    #             log.info("网络恢复正常了")
    #             return state
    #     elif state == 1:
    #         log.info("飞行模式")
    #         self.save_webImgs(model="飞行模式")
    #         self.exit_and_overRun() 
    #     else:
    #         log.info("网络正常")
    #         return True
    def get_getWebState(self,loop=1):
        state = run('ping www.baidu.com',stdout=PIPE,stderr=PIPE,stdin=PIPE,shell=True)
        # print("r=====",state.returncode)
        if state.returncode == 0:
            log.info("网络正常")
            return True
        else:
            log.info("无网络连接")
            self.save_webImgs(model="无网络连接")
            if loop > 0:
                time.sleep(30)
                if self.get_getWebState(loop-1):
                    return 6
            else:
                self.exit_and_overRun()
            
            
            

    # 查找一个元素
    def get_element(self, loc, model=None):
        log.info("{0}：获取元素 {1}".format(model, loc))
        try:
            return self.driver.find_element(*loc)
        except:
            if self.get_getWebState() == 6:
                self.get_element(loc, model=model)
            if self.check_page_popUp():
                return self.get_element(loc, model=model)
            else:
                log.exception("获取元素失败:{}".format(loc))
                # 截图
                self.save_webImgs(model)
                self.exit_and_overRun()

    # 查找一个元素
    def find_element(self, loc):
        return self.driver.find_element(*loc)

    # 查找相同的元素
    def find_elements(self, loc):
        return self.driver.find_elements(*loc)
        

    def get_elements(self, loc, model=None):
        log.info("{}".format(model))
        try:
            return self.driver.find_elements(*loc)
        except:
            if self.get_getWebState() == 6:
               self.get_elements(loc, model=model) 
            if self.check_page_popUp():
                return self.get_elements(loc, model=model)
            else:
                log.exception("定位元素失败")
                self.save_webImgs(model)
                self.exit_and_overRun()

    # 输入操作
    def input_text(self, loc, text, model=None):
        # 查找元素
        ele = self.get_element(loc,model=model)
        # 输入操作
        log.info("{0}: 在元素 {1} 中输入文本：{2}".format(model, loc, text))
        try:
            ele.send_keys(text)
        except:
            if self.get_getWebState() == 6:
               self.input_text(loc,text, model=model) 
            if self.check_page_popUp():
                return self.input_text(loc,text, model=model)
            else:
                log.exception("输入操作失败")
                # 截图
                self.save_webImgs(model)
                self.exit_and_overRun()

    # 清除操作
    def clear_input_text(self, loc, model=None):
        # 找元素再清除
        ele = self.get_element(loc, model=model)
        # 点击操作
        log.info("{0}: 元素：{1} 清除文本内容。".format(model, loc))
        try:
            ele.clear()
        except:
            if self.get_getWebState() == 6:
                self.clear_input_text(loc, model=model)
            if self.check_page_popUp():
                self.clear_input_text(loc, model=model)
            else:
                # 捕获异常到日志中；
                log.exception("元素：{0} 清除文本内容失败。：".format(loc))
                # 截图 - 保存到的指定的目录。名字要想好怎么取？
                self.save_webImgs(model)
                self.exit_and_overRun()

    # 点击操作
    def click_element(self, loc, model=None):
        
        try:
            if EC.element_to_be_clickable(loc) and self.isEnabled(loc,model="是否可点击"):
                # 找到元素
                ele = self.get_element(loc, model=model)
                time.sleep(1)
                ele.click()
                return True
            else:
                log.exception("点击元素:{0} 点击失败".format(loc))
                # 截图 - 保存到的指定的目录。名字要想好怎么取？
                self.save_webImgs(model)
                return False
        except:
            if self.get_getWebState() == 6:
                return self.click_element(loc, model=model)
            item = self.check_page_popUp()
            if item == PopUpLocator.close_broadcast:
                log.info("=========聊天室已关闭==========")
                self.exit_and_overRun()
            elif item:
                self.click_element(loc, model=model)
            else:
                # 捕获异常到日志中；
                log.exception("点击元素:{0} 点击事件失败".format(loc))
                # 截图 - 保存到的指定的目录。名字要想好怎么取？
                self.save_webImgs(model)
                return False
            
    def isEnabled(self,loc,model=None):
        if self.is_element_exist(loc):
            ele = self.get_element(loc,model=model)
            return ele.is_enabled()
        else:
            return False
    
    # 判断元素是否可点击
    def is_clickable(self, loc, model):
        try:
            if EC.element_to_be_clickable(loc) and self.isEnabled(loc,model=model):
                return True
        except:
            return False
                

    # 点击操作
    def click_element_byEle(self, ele, model=None):
        # 点击操作
        log.info("{0}: 元素：{1} 点击事件。".format(model, ele))
        try:
            ele.click()
            return True
        except:
            if self.get_getWebState() == 6:
                self.click_element_byEle(ele, model=model)
            if self.check_page_popUp():
                return self.click_element_byEle(ele, model=model)
            else:
                # 捕获异常到日志中；
                log.exception("元素:{0} 点击事件失败:".format(ele))
                # 截图 - 保存到的指定的目录。名字要想好怎么取？
                self.save_webImgs(model)
                self.exit_and_overRun()

    # 获取文本内容
    def get_text(self, loc, model=None):
        # 找到元素
        ele = self.get_element(loc, model=model)
        # 获取元素的文本内容
        try:
            text = ele.get_attribute("text")
            log.info("{0}：元素：{1} 的文本内容为：{2}".format(model, loc, text))
            return text
        except:
            if self.get_getWebState() == 6:
                self.get_text(loc, model=model)
            if self.check_page_popUp():
                return self.get_text(loc, model=model)
            else:
                # 捕获异常到日志中；
                log.exception("获取元素：{0} 的文本内容失败。报错信息如下：".format(loc))
                # 截图 - 保存到的指定的目录。名字要想好怎么取？
                self.save_webImgs(model)
                self.exit_and_overRun()

    # 获取元素的属性
    def get_element_attribute(self, loc, attr_name, model=None):
        # 找到元素
        ele = self.get_element(loc, model=model)
        # 获取元素的属性
        log.info("{0}: 获取元素：{1} 的属性：{2}".format(model, loc, attr_name))
        try:
            value = ele.get_attribute(attr_name)
            log.info("{0}: 元素：{1} 的属性：{2} 值为：{3}".format(model, loc, attr_name, value))
            return value
        except:
            if self.get_getWebState() == 6:
               self.get_element_attribute(loc, attr_name, model=model) 
            if self.check_page_popUp():
                return self.get_element_attribute(loc, attr_name, model=model)
            else:
                # 捕获异常到日志中；
                log.exception("获取元素：{0} 的属性：{1} 失败，异常信息如下：".format(loc, attr_name))
                # 截图 - 保存到的指定的目录。名字要想好怎么取？
                self.save_webImgs(model)
                self.exit_and_overRun()

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
            return True
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
            return True
        except:
            if self.get_getWebState() == 6:
                self.tap_by_coordinate(size,times=times, model=model)
            if self.check_page_popUp():
                return self.tap_by_coordinate(size,times=times, model=model)
            else:
                log.exception("等待元素可见失败。")
                # 截图
                self.save_webImgs(model)
                self.exit_and_overRun()

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
            self.exit_and_overRun()

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
    def get_toast_msg(self, part_text, model=None,t=5,s=0.03):
        # xpath表达式
        xpath_loc = '//*[contains(@text,"{}")]'.format(part_text)
        log.info("{0}: 获取toast信息，表达式为：{1}".format(model, xpath_loc))
        try:
            # 等待元素存在
            WebDriverWait(self.driver, t, s).until(EC.presence_of_element_located((MobileBy.XPATH, xpath_loc)))
            return self.get_element((MobileBy.XPATH, xpath_loc),model=model).text
        except:
            # 抛异常
            log.exception("获取toast失败")
            self.save_webImgs(model)
            return False


    def get_toast_exist(self,message,model=None,t=5,s=0.02):
        xpath_loc = '//*[contains(@text,"{}")]'.format(message)
        try:
            WebDriverWait(self.driver, t, s).until(EC.presence_of_element_located((MobileBy.XPATH, xpath_loc)))
            return self.get_element((MobileBy.XPATH, xpath_loc),model=model).text
        except:
            return "" #"获取toast失败"

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


    # 判断元素是否存在
    def is_element_exist(self, loc, timeout=5, poll_frequency=0.5, model=None):
        try:
            el = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
            return True
        except:
            if self.get_getWebState() == 6:
                log.info("断网重连ok")
                self.is_element_exist(loc,timeout=timeout, poll_frequency=poll_frequency, model=model)
            pagepop = self.check_page_popUp()
            if pagepop:
                log.info("关闭了{}弹窗".format(pagepop))
                return self.is_element_exist(loc,timeout=timeout, poll_frequency=poll_frequency, model=model)
            else:
                return False
        

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

    
    def check_page_popUp(self):
        time.sleep(2)
        source = self.driver.page_source
        element = ""
        for i in PopUpLocator.popList:
            log.info("检测页面弹窗:{}".format(i))
            if i[1] in source:
                self.click_element(i)
                element = i
                break
        return element
    
    def close_page_popUp(self):
        if self.check_page_popUp():
           self.check_page_popUp() 
        else:
            pass

    #退出app，结束程序运行
    def exit_and_overRun(self):
        self.driver.close_app()
        self.driver.quit()


    def wait_click_element(self,loc,model,timeout=5):
        if self.wait_element_clickable(loc,timeout=timeout,model="等待{}".format(model)):
            self.click_element(loc,model="点击{}".format(model))
        
    def wait_input_text(self,loc,text,model):
        self.wait_element_presence(loc,model="等待{}输入框".format(model))
        self.clear_input_text(loc,model="清除旧{}".format(model))
        self.input_text(loc,text,model="输入新{}".format(model))