import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.room_page import RoomPage
from Pages.pageObjects.Common_Buss import CommonBus as  Cb
from Pages.pageLocators.room_locators import RoomPageLocator
log = get_logger(logger_name="首页操作日志")


@pytest.mark.run(order=1)
@allure.feature('房间模块') #模块名
class TestRoomMakeFriends:

    @pytest.mark.success
    @allure.story('进入推荐聊天室')
    @allure.title('进入推荐聊天室')
    def test_recommend_Room(self, startApp_keepUserData):
        room_page = RoomPage(startApp_keepUserData)
        common_func = Cb(startApp_keepUserData)
        log.info("**************房间模块-推荐tap-进退聊天室****************")
        room_page.find_room() #点击房间模块
        room_page.room_tap(RoomPageLocator.recommend_tap) #点击推荐tap
        room_page.check_MinorSettings() #检测未成年弹框
        room_page.driver.implicitly_wait(8)
        liveRoomMum = room_page.enter_liveRoom() #进入聊天室
        with allure.step("进入推荐聊天室"):
            try:
                assert liveRoomMum == True
                log.info("进入推荐聊天室断言成功")
            except AssertionError as a:
                log.error("进入推荐聊天室断言失败")
                common_func.save_webImgs("进入推荐聊天室-断言截图")
                raise a

    # @pytest.mark.success
    # @allure.story('进入派对聊天室')
    # @allure.title('进入派对聊天室')
    # def test_party_Room(self, startApp_keepUserData):
    #     room_page = RoomPage(startApp_keepUserData)
    #     common_func = Cb(startApp_keepUserData)
    #     log.info("**************房间模块-派对tap-进退房间****************")
    #     room_page.find_room() #点击房间模块
    #     room_page.room_tap(RoomPageLocator.party_tap) #点击派对tap
    #     room_page.check_MinorSettings() #检测未成年弹框
    #     room_page.driver.implicitly_wait(8)
    #     liveRoomMum = room_page.open_party_room() #进入派对聊天室
    #     with allure.step("进入派对聊天室"):
    #         try:
    #             assert liveRoomMum == True
    #             log.info("进入派对聊天室断言成功")
    #         except AssertionError as a:
    #             log.error("进入派对聊天室断言失败")
    #             common_func.save_webImgs("进入派对聊天室-断言截图")
    #             raise a

    # @pytest.mark.success
    # @allure.story('进入开黑聊天室')
    # @allure.title('进入开黑聊天室')
    # def test_openBlack_Room(self, startApp_keepUserData):
    #     room_page = RoomPage(startApp_keepUserData)
    #     common_func = Cb(startApp_keepUserData)
    #     log.info("**************房间模块-开黑tap-进退房间****************")
    #     room_page.find_room() #点击房间模块
    #     room_page.room_tap(RoomPageLocator.open_black_tap) #点击开黑tap
    #     room_page.check_MinorSettings() #检测未成年弹框
    #     room_page.driver.implicitly_wait(8)
    #     liveRoomMum = room_page.open_black_room() #进入聊天室
    #     with allure.step("进入开黑聊天室"):
    #         try:
    #             assert liveRoomMum == True
    #             log.info("进入开黑聊天室断言成功")
    #         except AssertionError as a:
    #             log.error("进入开黑聊天室断言失败")
    #             common_func.save_webImgs("进入开黑聊天室-断言截图")
    #             raise a

    # @pytest.mark.success
    # @allure.story('创建小窝类型的聊天室')
    # @allure.title('创建一个小窝类型的聊天室')            
    # def test_establish_bathmos_Room(self, startApp_keepUserData):
    #     room_page = RoomPage(startApp_keepUserData)
    #     common_func = Cb(startApp_keepUserData)
    #     log.info("**************创建小窝类型的聊天室****************")
    #     liveRoomMum = room_page.found_minNest_room()
    #     with allure.step("@创建小窝类型的聊天室@"):
    #         try:
    #             assert liveRoomMum == True
    #             log.info("创建小窝类型的聊天室断言成功")
    #         except AssertionError as a:
    #             log.error("创建小窝类型的聊天室断言失败")
    #             common_func.save_webImgs("创建小窝类型聊天室-断言截图")
    #             raise a

    # @pytest.mark.success
    # @allure.story('创建萌新接待类型的聊天室')
    # @allure.title('创建一个萌新接待类型的聊天室')            
    # def test_establish_reception_Room(self, startApp_keepUserData):
    #     room_page = RoomPage(startApp_keepUserData)
    #     common_func = Cb(startApp_keepUserData)
    #     log.info("**************创建萌新接待类型的聊天室****************")
    #     liveRoomMum = room_page.found_reception_room()
    #     with allure.step("@创建萌新接待类型的聊天室@"):
    #         try:
    #             assert liveRoomMum == True
    #             log.info("创建萌新接待类型的聊天室断言成功")
    #         except AssertionError as a:
    #             log.error("创建萌新接待类型的聊天室断言失败")
    #             common_func.save_webImgs("创建萌新接待类型聊天室-断言截图")
    #             raise a


        # log.info("***************首页进出关播人员主页*****************")
        # enter_notLiveRoom = home_page.enter_notLiveRoom()
        # with allure.step("进出关播人员主页"):
        #     try:
        #         assert int(enter_notLiveRoom) > 0
        #         log.info("进出关播人员主页断言成功")
        #     except AssertionError as a:
        #         log.error("进出关播人员主页断言失败")
        #         common_func.save_webImgs("进出关播人员主页-断言截图")
        #         raise a

    #     log.info("****************首页进出关播人员主页测试用例*******************")
    #     actual_moneytotalrank = hot_page.moneytotalrank()
    #     with allure.step("热门排行榜财富总榜测试用例"):
    #         try:
    #             assert int(actual_moneytotalrank) > 0
    #             log.error("热门排行榜财富总榜测试用例")
    #         except AssertionError as a:
    #             log.error("断言失败")
    #             common_func.save_webImgs("热门排行榜财富总榜测试用例-断言-截图")
    #             raise a

    #     log.info("***********************************热门排行榜礼物星榜测试用例-测试用例**************************************")

    #     # actual_starrank = hot_page.starrank()
    #     # with allure.step("热门排行榜礼物星榜测试用例"):
    #     #     try:
    #     #         assert actual_starrank == "换个姿势重来一次"
    #     #         log.error("热门排行榜礼物星榜测试用例-测试用例通过")
    #     #     except AssertionError as a:
    #     #         log.error("断言失败")
    #     #         common_func.save_webImgs("热门排排行榜礼物星榜测试用例-断言-截图")
    #     #         raise a

    #     # log.info("***********************************热门守护总榜查看测试用例-测试用例**************************************")

    #     # actual_guardian = hot_page.guardian()
    #     # with allure.step("热门守护总榜查看测试用例"):
    #     #     try:
    #     #         assert actual_guardian == True
    #     #         log.error("热门守护总榜查看测试用例-测试用例通过")
    #     #     except AssertionError as a:
    #     #         log.error("断言失败")
    #     #         hot_page.save_webImgs("热门守护总榜查看测试用例-断言-截图")
    #     #         raise a

    # @pytest.mark.message
    # @allure.story('消息页面用例')
    # @allure.title('消息页面用例')
    # def test_message(self, startApp_keepUserData):
    #     hot_page = HotPage(startApp_keepUserData)
    #     log.info("***********************************热门进入消息页面测试用例-测试用例**************************************")
    #     actual_message = hot_page.into_hot().message()
    #     with allure.step("热门进入消息页面测试用例"):
    #         try:
    #             assert actual_message == "消息"
    #             log.error("热门进入消息页面测试用例-测试用例通过")
    #         except AssertionError as a:
    #             log.error("断言失败")
    #             hot_page.save_webImgs("热门进入消息页面测试用例-断言-截图")
    #             raise a

    # @pytest.mark.morepage
    # @allure.story('筛选页面用例')
    # @allure.title('筛选页面用例')
    # def test_morepage(self, startApp_keepUserData):
    #     log.info("***********************************热门进入到筛选页面测试用例-测试用例**************************************")
    #     hot_page = HotPage(startApp_keepUserData)
    #     actual_morepage = hot_page.into_hot().morepage()
    #     with allure.step("热门进入到筛选页面测试用例"):
    #         try:
    #             assert actual_morepage is True
    #             log.error("热门进入到筛选页面测试用例-测试用例通过")
    #         except AssertionError as a:
    #             log.error("断言失败")
    #             hot_page.save_webImgs("热门进入到筛选页面测试用例-断言-截图")
    #             raise a

    #     log.info("***********************************热门标签选择页面测试用例-测试用例**************************************")

    #     actual_showAllLabel = hot_page.showAllLabel()
    #     with allure.step("热门标签选择页面测试用例"):
    #         try:
    #             assert actual_showAllLabel == "Uplive"
    #             log.error("热门标签选择页面测试用例-测试用例通过")
    #         except AssertionError as a:
    #             log.error("断言失败")
    #             hot_page.save_webImgs("热门标签选择页面测试用例-断言-截图")
    #             raise a


if __name__ == '__main__':
    pytest.main(['-s', './test_hot.py', '--alluredir', 'temp'])
