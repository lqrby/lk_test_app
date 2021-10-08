'''
Author: your name
Date: 2021-09-06 15:59:49
LastEditTime: 2021-10-08 11:24:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /lk_test_app/Test_Cases/test_homeMakeFriends.py
'''
import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.room_page import RoomPage
from Pages.pageObjects.Common_Buss import CommonBus as  Cb
 

log = get_logger(logger_name="首页操作日志")


@pytest.mark.run(order=1)
@allure.feature('首页(交友)') #模块名
class TestHomeMakeFriends:
    '''
    发现-用户进入的聊天室
    '''
    @pytest.mark.success
    @allure.story('首页(交友)')
    @allure.title('首页(交友)')
    def test_inToRoom(self, startApp_keepUserData):
        room_page = RoomPage(startApp_keepUserData)
        common_func = Cb(startApp_keepUserData)
        log.info("**************首页(交友)-发现tap下查看用户进入的聊天室****************")
        liveRoomMum = room_page.enter_liveRoom()
        with allure.step("进出开播房间"):
            try:
                assert liveRoomMum == True
                log.info("进出开播房间断言成功")
            except AssertionError as a:
                log.error("进出开播房间断言失败")
                common_func.save_webImgs("进入开播房间-断言截图")
                raise a


    '''
    发现-用户资料页
    '''
    @pytest.mark.success
    @allure.story('首页(交友)')
    @allure.title('首页(交友)')
    def test_NoInToRoom(self, startApp_keepUserData):
        log.info("***************首页(交友)---发现tap---查看用户资料页*****************")
        room_page = RoomPage(startApp_keepUserData)
        common_func = Cb(startApp_keepUserData)
        enter_notLiveRoom = room_page.enter_notLiveRoom()
        with allure.step("查看用户主页"):
            try:
                assert len(enter_notLiveRoom) > 0
                log.info("查看用户主页断言成功")
            except AssertionError as a:
                log.error("查看用户主页断言失败")
                common_func.save_webImgs("查看用户主页-断言截图")
                raise a


    '''附近的人-用户资料页'''  
    @pytest.mark.success
    @allure.story('首页-附近的人-用户资料')
    @allure.title('首页-附近的人-用户资料')          
    def test_peopleNearby(self, startApp_keepUserData):
        log.info("************首页---附近的人--- 用户主页资料*************")
        room_page = RoomPage(startApp_keepUserData)
        common_func = Cb(startApp_keepUserData)
        nearby_people_dataPage = room_page.nearby_people_dataPage()
        with allure.step("查看附近的人主页资料"):
            try:
                assert len(nearby_people_dataPage) > 0
                log.info("查看附近的人主页资料断言成功")
            except AssertionError as a:
                log.error("查看附近的人主页资料断言失败")
                common_func.save_webImgs("查看附近的人主页资料-断言截图")
                raise a


    '''附近的人-用户进入的聊天室'''   
    @pytest.mark.success
    @allure.story('首页-附近的人-聊天室')
    @allure.title('首页-附近的人-聊天室')          
    def test_peopleNearby_room(self, startApp_keepUserData):
        log.info("************首页---附近的人--- 用户进入的聊天室*************")
        room_page = RoomPage(startApp_keepUserData)
        common_func = Cb(startApp_keepUserData)
        nearby_people_chatRoom = room_page.nearby_people_chatRoom()
        with allure.step("进退附近的人进入的聊天室"):
            try:
                assert nearby_people_chatRoom == True
                log.info("进退附近的人进入的聊天室断言成功")
            except AssertionError as a:
                log.error("进退附近的人进入的聊天室断言失败")
                common_func.save_webImgs("进退附近的人进入的聊天室-断言截图")
                raise a

    
    '''附近动态'''            
    def test_nearbyDynamics(self, startApp_keepUserData):
        log.info("************首页---附近动态---*************")
        room_page = RoomPage(startApp_keepUserData)
        common_func = Cb(startApp_keepUserData)
        nearby_dynamics = room_page.nearby_dynamics()
        with allure.step("查看附近动态"):
            try:
                assert len(nearby_dynamics) > 0
                log.info("查看附近动态断言成功")
            except AssertionError as a:
                log.error("查看附近动态断言失败")
                common_func.save_webImgs("查看附近动态-断言截图")
                raise a

    

if __name__ == '__main__':
    pytest.main(['-s', './test_hot.py', '--alluredir', 'temp'])
