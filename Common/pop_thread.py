"""
======================
@author：liang.wang
@time:2021/3/21-8:48 下午
======================
"""
import threading
import time

from Common.log import get_logger
from Pages.pageObjects.sign_pop_page import SignPopPage

log = get_logger(logger_name="pop操作日志")


class PopThread(threading.Thread):
    """
    弹窗线程监测
    pop_list：弹窗数据源存在的元素
    """

    def __init__(self, driver, pop_list):
        threading.Thread.__init__(self)
        self.driver = driver
        self.pop_list = pop_list

    def run(self):
        # print("开始线程")
        self.pop()
        # print("线程结束")

    def pop(self):
        while True:
            # print("循环获取数据源")
            try:
                time.sleep(2)
                source = self.driver.page_source
                # print(source)
                for i in self.pop_list:
                    # log.info("循环查找pop")
                    if i in source:
                        pop = SignPopPage(self.driver, i)
                        pop.close_ivClose().closeGameInvit().skipAD().systempop().locatpop().privacy().test_ad().\
                            check_bounced().is_Begintolive().close_language().Adolescent_model()
            except Exception as e:
                print(e)
