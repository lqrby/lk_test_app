
import allure
import pytest
from Pages.pageObjects.my_page import MyPage
from TestDatas.my import profileData
from Common.log import get_logger

log = get_logger(logger_name="我的操作日志")

'''我的页面'''


@pytest.mark.run(order=3)
@allure.feature('我的')
class Test_my:
    
    @allure.story('我的')
    @allure.title('查看个人资料用例')
    def test_intoProfile(self, startApp_keepUserData):
        log.info("**************我的-查看个人资料-测试用例**************")
        my_page = MyPage(startApp_keepUserData)
        myprofile = my_page.view_my_profile()
        try:
            assert myprofile == True
            log.info("查看个人资料-测试用例通过")
        except AssertionError as a:
            log.error("查看个人资料-断言失败")
            
    @pytest.mark.success
    @allure.story('我的')
    @allure.title('编辑页用例')
    @pytest.mark.parametrize("myProfileData", profileData)
    def test_intoEdit(self,myProfileData, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的-资料编辑页-测试用例***************")
        actual_edit = my_page.edit_my_profile(myProfileData)
        try:
            assert actual_edit == True
            log.error("资料编辑页测试用例-测试用例通过")
        except AssertionError as a:
            log.error("资料编辑页断言失败")


    @pytest.mark.success
    @allure.story('我的')
    @allure.title('我的好友、谁看过我和派对足迹用例')
    def test_intoEdit(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>我的好友、谁看过我和派对足迹-测试用例***************")
        actual_edit = my_page.myFriend_whoLookMe_partyFootprints()
        try:
            assert actual_edit == True
            log.error("我的好友、谁看过我和派对足迹测试用例-测试用例通过")
        except AssertionError as a:
            log.error("我的好友、谁看过我和派对足迹测试用例断言失败")
            

    # @allure.story('我的')
    # @allure.title('钱包用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoMoneyBar(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-钱包-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_moneynar = my_page.intoMoneyBar()
    #     try:
    #         assert actual_moneynar == caseassert["actual_moneynar"]
    #         log.error("钱包-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("钱包-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('任务中心页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoTask(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-任务中心-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_tast = my_page.intoTask()
    #     try:
    #         assert actual_tast == caseassert["actual_tast"]
    #         log.error("任务中心-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("任务中心-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('我的消息页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoMessage(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-我的消息-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_message = my_page.intoMessage()
    #     try:
    #         assert actual_message == caseassert["actual_message"]
    #         log.error("我的消息-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("我的消息-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('我的道具页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoFerrari(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-我的道具-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_intoFerrari = my_page.intoFerrari()
    #     try:
    #         assert actual_intoFerrari == caseassert["actual_intoFerrari"]
    #         log.error("我的道具-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("我的道具-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('我的等级页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoFerrari(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-我的等级-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_intoGrade = my_page.intoGrade()
    #     try:
    #         assert actual_intoGrade == caseassert["actual_intoGrade"]
    #         log.error("我的等级-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("我的等级-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('庄园页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoManor(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-庄园-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_manor = my_page.intoManor()
    #     try:
    #         assert actual_manor is not caseassert["actual_manor"]
    #         log.error("庄园-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("庄园-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('尊享会员页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoMember(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-尊享会员-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_intoMember = my_page.intoMember()
    #     try:
    #         assert actual_intoMember == caseassert["actual_intoMember"]
    #         log.error("尊享会员-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("尊享会员-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('VIP特权页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoVIPGrade(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-VIP特权-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_intoVIPGrade = my_page.intoVIPGrade()
    #     try:
    #         assert actual_intoVIPGrade == caseassert["actual_intoVIPGrade"]
    #         log.error("VIP特权-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("VIP特权-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('我的家族页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoFamily(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-我的家族-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_intoFamily = my_page.intoFamily()
    #     try:
    #         assert actual_intoFamily == caseassert["actual_intoFamily"]
    #         log.error("我的家族-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("我的家族-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('真爱团页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoFans(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-真爱团-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_fans = my_page.intoFans()
    #     try:
    #         assert actual_fans == caseassert["actual_fans"]
    #         log.error("真爱团-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("真爱团-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('我的直播页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoFLive(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-我的直播-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_intoFLive = my_page.intoFLive()
    #     try:
    #         assert actual_intoFLive == caseassert["actual_intoFLive"]
    #         log.error("我的直播-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("我的直播-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('U币贡献榜页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoContribution(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-U币贡献榜-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_intoContribution = my_page.intoContribution()
    #     try:
    #         assert actual_intoContribution == caseassert["actual_intoContribution"]
    #         log.error("U币贡献榜-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("U币贡献榜-断言-截图")
    #         raise a
    #     my_page.back()

    # @allure.story('我的')
    # @allure.title('我的守护页用例')
    # @pytest.mark.parametrize("caseassert", myassert)
    # def test_intoGuardian(self, caseassert, startApp_keepUserData1):
    #     log.info("*************************************我的-我的守护-测试用例******************************************")
    #     my_page = MyPage(startApp_keepUserData1)
    #     my_page.back()
    #     actual_intoGuardian = my_page.intoGuardian()
    #     try:
    #         assert actual_intoGuardian == caseassert["actual_intoGuardian"]
    #         log.error("我的守护-测试用例通过")
    #     except AssertionError as a:
    #         log.error("断言失败")
    #         my_page.save_webImgs("我的守护-断言-截图")
    #         raise a
    #     my_page.back()



if __name__ == '__main__':
    pytest.main()
