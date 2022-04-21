from Pages.pageObjects.Common_Buss import CommonBus
from Pages.pageLocators.square_locators import SquareLocators as squareloc
from Common.log import get_logger
import time, random
from Pages.pageObjects.sign_pop_page import SignPopPage
from Pages.pageLocators.room_locators import RoomPageLocator as roomloc
from Pages.pageObjects.room_page import RoomPage

'''设置-页面操作行为'''
log = get_logger(logger_name="广场操作日志")

class SquarePage(CommonBus):
    '''广场模块'''
    def __init__(self, driver):
        self.driver = driver
        self.popPage = SignPopPage(self.driver)
        self.roomPage = RoomPage(self.driver)
    
    '''
    附近动态流程
    '''
    def nearby_dynamics(self):
        self.wait_click_element(squareloc.square_module,model="广场模块")
        time.sleep(2)
        return self.dynamicDetailPageAssertion()
        
    #附近动态tap
    def nearby_dynamics_tap(self):
        self.wait_element_clickable(roomloc.tv_content,model="关注按钮是否可点击")
        self.click_element(roomloc.tv_content,model="点击关注tap")

    #附近动态列表-进入动态详情
    def nearby_dynamics_list(self):
        nearbyDynamicsList = self.is_element_exist(squareloc.tv_content,model="附近动态列表")
        if nearbyDynamicsList == True:
            nearby_dynamicsList = self.get_elements(squareloc.tv_content,model="获取动态列表") 
            log.info("列表数据有{}条".format(len(nearby_dynamicsList)))
            dt_num = random.randint(0,len(nearby_dynamicsList)-1) 
            log.info("点击第{}个动态查看详情".format(dt_num))
            time.sleep(3)
            nearby_dynamicsList[dt_num].click()
            time.sleep(5)
            if self.is_element_exist(squareloc.tvnick,model="昵称"):
                self.assert_true(squareloc.tvnick,model="昵称")
                return "1"
            elif self.is_element_exist(squareloc.masterAvatarView,model="打赏礼物入口"):
                self.assert_true(squareloc.masterAvatarView,model="断言打赏礼物入口")
                self.roomPage.exit_chat_room()
                return "2"
            else:
                log.info("断言失败！请及时处理！！！")
                self.save_webImgs("查看用户主页断言失败")
                return "3"
        else:
            nearbyDynamicsList2 = self.is_element_exist(squareloc.nearby_dynamics_list2,model="附近动态列表2") 
            if nearbyDynamicsList2 == True:
                nearby_dynamicsList = self.get_elements(squareloc.nearby_dynamics_list2,model="获取动态列表2") 
                log.info("列表数据有{}条".format(len(nearby_dynamicsList)))
                dt_num = random.randint(0,len(nearby_dynamicsList)-1) 
                log.info("点击第{}个动态查看详情".format(dt_num))
                nearby_dynamicsList[dt_num].click()
                time.sleep(5)
                if self.is_element_exist(squareloc.tvnick,model="昵称"):
                    self.assert_true(squareloc.tvnick,model="昵称")
                    return "1"
                elif self.is_element_exist(squareloc.masterAvatarView,model="礼物入口1"):
                    self.assert_true(squareloc.masterAvatarView,model="断言打赏礼物入口")
                    self.roomPage.exit_chat_room()
                    return "2"
                else:
                    log.info("断言失败！请及时处理！！！")
                    self.save_webImgs("查看用户主页断言失败")
                    return "3"
            else:
                log.info("动态列表暂无数据")
                self.save_webImgs("动态列表暂无数据")
                return "4"

    #点赞
    def spot_fabulous(self,repeat=9):
        bool = self.is_element_exist(squareloc.iv_prise,model="点赞元素")
        if bool == False and repeat > 0:
            repeat = repeat - 1
            self.swipeUp()
            self.spot_fabulous(repeat)
        ivprise = self.is_clickable(squareloc.iv_prise,model="点赞元素")
        log.info(ivprise)
        if ivprise :
            time.sleep(1)
            self.click_element(squareloc.iv_prise,model="点击点赞")
        else:
            log.info("已点过赞了")

    
    #关注
    def click_follow(self):
        if self.is_clickable(squareloc.follow,model="关注是否可点击"):
            time.sleep(1)
            self.click_element(squareloc.follow,model="点击关注")
            gz_toast = "关注成功"
            followSuccess = self.get_toast_msg(gz_toast, model="关注成功的toast")
            self.assert_in(gz_toast, followSuccess, model="关注用户") #断言关注
        else:
            log.info("已关注,不可再点击关注")

    #举报
    def reportBtn(self):
        self.wait_element_clickable(squareloc.reportBtn,model="举报按钮是否可点击")
        self.click_element(squareloc.reportBtn,model="点击举报按钮")
        time.sleep(1)

    ''' 广场-关注-动态'''
    def square_attention(self):
        self.wait_click_element(squareloc.square_module,model="广场模块")
        time.sleep(2)
        self.wait_click_element(squareloc.square_attention,model="关注")
        return self.dynamicDetailPageAssertion()

    #动态详情页断言
    def dynamicDetailPageAssertion(self):
        dt_detail = self.nearby_dynamics_list() #动态列表随机-进入动态详情，并断言
        if dt_detail == "1":
            self.spot_fabulous() #点赞
            self.click_follow() #关注
            self.roomPage.click_more() #点击更多
            self.reportBtn() #举报
            self.assert_true(squareloc.commitBtn,model="举报断言") #举报断言
            self.roomPage.go_back() #返回详情页
            self.roomPage.go_back_list() #返回列表页
            return True
        elif dt_detail == "2":
            log.info("该用户正在聊天室嗨皮呢，所以未进入ta的主页，进入了ta所在的聊天室")
            return True
        elif dt_detail == "4":
            return True
        else:
            return False