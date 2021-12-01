'''
Author: your name
Date: 2021-09-06 15:59:49
LastEditTime: 2021-11-02 10:22:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Test_Cases/test_homeMakeFriends.py
'''
import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.room_page import RoomPage
from Pages.pageObjects.square_page import SquarePage
from Pages.pageObjects.Common_Buss import CommonBus as  Cb
 

log = get_logger(logger_name="首页操作日志")


@pytest.mark.run(order=2)
@allure.feature('首页(交友)') #模块名
class TestHomeMakeFriends:
    '''
    发现-用户进入的聊天室
    '''
    @pytest.mark.success
    @allure.story('首页(交友)-发现-聊天室')
    @allure.title('首页(交友)-发现-聊天室')
    def test_inToRoom(self, startApp_keepUserData):
        room_page = RoomPage(startApp_keepUserData)
        log.info("**************首页(交友)-发现tap下查看用户进入的聊天室****************")
        liveRoomMum = room_page.enter_liveRoom()
        with allure.step("进出开播房间"):
            try:
                assert liveRoomMum == True
                log.info("进出开播房间断言成功")
            except AssertionError as a:
                log.error("进出开播房间断言失败")
                raise

    '''
    发现-用户资料页
    '''
    @pytest.mark.success
    @allure.story('首页(交友)-发现-用户资料')
    @allure.title('首页(交友)-发现-用户资料')
    def test_NoInToRoom(self, startApp_keepUserData):
        log.info("***************首页(交友)---发现tap---查看用户资料页*****************")
        room_page = RoomPage(startApp_keepUserData)
        enter_notLiveRoom = room_page.enter_notLiveRoom()
        with allure.step("查看用户主页"):
            try:
                assert enter_notLiveRoom == True
                log.info("查看用户主页断言成功")
            except AssertionError as a:
                log.error("查看用户主页断言失败")
                raise


    '''附近的人-用户资料页'''  
    @pytest.mark.success
    @allure.story('首页-附近的人-用户资料')
    @allure.title('首页-附近的人-用户资料')          
    def test_peopleNearby(self, startApp_keepUserData):
        log.info("************首页---附近的人--- 用户主页资料*************")
        room_page = RoomPage(startApp_keepUserData)
        nearby_people_dataPage = room_page.nearby_people_dataPage()
        with allure.step("查看附近的人主页资料"):
            try:
                assert nearby_people_dataPage == True
                log.info("查看附近的人主页资料断言成功")
            except AssertionError as a:
                log.error("查看附近的人主页资料断言失败")
                raise


    '''附近的人-用户进入的聊天室'''   
    @pytest.mark.success
    @allure.story('首页-附近的人-聊天室')
    @allure.title('首页-附近的人-聊天室')          
    def test_peopleNearby_room(self, startApp_keepUserData):
        log.info("************首页---附近的人--- 用户进入的聊天室*************")
        room_page = RoomPage(startApp_keepUserData)
        nearby_people_chatRoom = room_page.nearby_people_chatRoom()
        with allure.step("进退附近的人进入的聊天室"):
            try:
                assert nearby_people_chatRoom == True
                log.info("进退附近的人进入的聊天室断言成功")
            except AssertionError as a:
                log.error("进退附近的人进入的聊天室断言失败")
                raise

    
    

    

if __name__ == '__main__':
    pytest.main(['-s', './test_hot.py', '--alluredir', 'temp'])
