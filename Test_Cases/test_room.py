import allure
import pytest, time
from Common.log import get_logger
from Pages.pageObjects.room_page import RoomPage
from Pages.pageObjects.Common_Buss import CommonBus as  Cb
from Pages.pageLocators.room_locators import RoomPageLocator
from appium_sync.appium_devices_sync import devices_star_sync
from Pages.pageObjects.sign_pop_page import SignPopPage
log = get_logger(logger_name="首页操作日志")


@pytest.mark.run(order=1)
@allure.feature('房间模块') #模块名
class TestRoomMakeFriends:
    @pytest.mark.success
    @allure.story('进入推荐聊天室')
    @allure.title('进入推荐聊天室')
    def test_recommend_Room(self, startApp_keepUserData):
        room_page = RoomPage(startApp_keepUserData)
        log.info("**************房间模块-推荐tap-进退聊天室****************")
        liveRoomMum = room_page.recommend_liveRoom() #进入推荐聊天室
        with allure.step("进入推荐聊天室"):
            try:
                assert liveRoomMum["result"] == True
                log.info("进入推荐聊天室断言成功")
            except AssertionError as a:
                log.error("进入推荐聊天室断言失败--{}".format(liveRoomMum["message"]))
                raise


    @pytest.mark.success
    @allure.story('进入派对聊天室')
    @allure.title('进入派对聊天室')
    def test_party_Room(self, startApp_keepUserData):
        room_page = RoomPage(startApp_keepUserData)
        log.info("**************房间模块-派对tap-进退房间****************")
        liveRoomMum = room_page.open_party_room() #进入派对聊天室
        with allure.step("进入派对聊天室"):
            try:
                assert liveRoomMum["result"] == True
                log.info("进入派对聊天室流程断言成功")
            except AssertionError as a:
                log.error("进入派对聊天室流程断言失败，失败原因:{}".format(liveRoomMum["message"]))
                raise


    @pytest.mark.success
    @allure.story('进入开黑聊天室')
    @allure.title('进入开黑聊天室')
    def test_openBlack_Room(self, startApp_keepUserData):
        room_page = RoomPage(startApp_keepUserData)
        log.info("**************房间模块-开黑tap-进退房间****************")
        liveRoomMum = room_page.open_black_room() #进入聊天室
        with allure.step("进入开黑聊天室"):
            try:
                assert liveRoomMum["result"] == True
                log.info("进入开黑聊天室断言成功")
            except AssertionError as a:
                log.error("进入开黑聊天室断言失败,失败原因:{}".format(liveRoomMum["message"]))
                raise


    @pytest.mark.success
    @allure.story('创建小窝类型的聊天室')
    @allure.title('创建一个小窝类型的聊天室')            
    def test_establish_bathmos_Room(self, startApp_keepUserData):
        room_page = RoomPage(startApp_keepUserData)
        log.info("**************创建小窝类型的聊天室****************")
        liveRoomMum = room_page.found_minNest_room()
        with allure.step("@创建小窝类型的聊天室@"):
            try:
                assert liveRoomMum != False
                log.info("创建小窝类型的聊天室断言成功")
            except AssertionError as a:
                log.error("创建小窝类型的聊天室断言失败")
                raise


    @pytest.mark.success
    @allure.story('创建萌新接待类型的聊天室')
    @allure.title('创建一个萌新接待类型的聊天室')            
    def test_establish_reception_Room(self, startApp_keepUserData):
        room_page = RoomPage(startApp_keepUserData)
        log.info("**************创建萌新接待类型的聊天室****************")
        liveRoomMum = room_page.found_reception_room()
        with allure.step("@创建萌新接待类型的聊天室@"):
            try:
                assert liveRoomMum == True
                log.info("创建萌新接待类型的聊天室断言成功")
            except AssertionError as a:
                log.error("创建萌新接待类型的聊天室断言失败")
                raise

       
    

    

    


if __name__ == '__main__':
    pytest.main(['-s', './test_hot.py', '--alluredir', 'temp'])
