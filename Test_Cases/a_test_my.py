'''
@File    :  test_my.py    
@Contact :  fangfang.song@asiainnovations.com

@Modify Time    2021/4/1 10:25 下午    
@Author  :  songfang  
@Version :  1.0
@Desciption : 
'''
import allure
import pytest
from Common.log import get_logger
from Pages.pageObjects.my_page import MyPage
from TsetDatas.my import myassert

log = get_logger(logger_name="我的操作日志")

'''我的页面'''


@pytest.mark.run(order=3)
@allure.feature('我的')
class Test_my:
    @pytest.mark.success
    @allure.story('我的')
    @allure.title('编辑页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoEdit(self, caseassert, startApp_keepUserData1):
        my_page = MyPage(startApp_keepUserData1)
        log.info("***********************************我的-资料编辑页-测试用例**************************************")
        my_page.back()
        actual_edit = my_page.my().intoEdit()
        try:
            assert actual_edit == caseassert["actual_edit"]
            log.error("资料编辑页测试用例-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("资料编辑页测试用例-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('个人资料页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoProfile(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-个人资料页-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        myprofile = my_page.intoProfile()
        try:
            assert myprofile is not caseassert["myprofile"]
            log.error("个人资料页-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("个人资料页-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('钱包用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoMoneyBar(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-钱包-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_moneynar = my_page.intoMoneyBar()
        try:
            assert actual_moneynar == caseassert["actual_moneynar"]
            log.error("钱包-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("钱包-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('任务中心页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoTask(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-任务中心-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_tast = my_page.intoTask()
        try:
            assert actual_tast == caseassert["actual_tast"]
            log.error("任务中心-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("任务中心-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('我的消息页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoMessage(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-我的消息-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_message = my_page.intoMessage()
        try:
            assert actual_message == caseassert["actual_message"]
            log.error("我的消息-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("我的消息-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('我的道具页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoFerrari(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-我的道具-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoFerrari = my_page.intoFerrari()
        try:
            assert actual_intoFerrari == caseassert["actual_intoFerrari"]
            log.error("我的道具-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("我的道具-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('我的等级页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoFerrari(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-我的等级-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoGrade = my_page.intoGrade()
        try:
            assert actual_intoGrade == caseassert["actual_intoGrade"]
            log.error("我的等级-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("我的等级-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('庄园页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoManor(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-庄园-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_manor = my_page.intoManor()
        try:
            assert actual_manor is not caseassert["actual_manor"]
            log.error("庄园-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("庄园-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('尊享会员页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoMember(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-尊享会员-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoMember = my_page.intoMember()
        try:
            assert actual_intoMember == caseassert["actual_intoMember"]
            log.error("尊享会员-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("尊享会员-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('VIP特权页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoVIPGrade(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-VIP特权-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoVIPGrade = my_page.intoVIPGrade()
        try:
            assert actual_intoVIPGrade == caseassert["actual_intoVIPGrade"]
            log.error("VIP特权-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("VIP特权-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('我的家族页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoFamily(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-我的家族-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoFamily = my_page.intoFamily()
        try:
            assert actual_intoFamily == caseassert["actual_intoFamily"]
            log.error("我的家族-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("我的家族-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('真爱团页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoFans(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-真爱团-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_fans = my_page.intoFans()
        try:
            assert actual_fans == caseassert["actual_fans"]
            log.error("真爱团-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("真爱团-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('我的直播页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoFLive(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-我的直播-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoFLive = my_page.intoFLive()
        try:
            assert actual_intoFLive == caseassert["actual_intoFLive"]
            log.error("我的直播-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("我的直播-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('U币贡献榜页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoContribution(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-U币贡献榜-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoContribution = my_page.intoContribution()
        try:
            assert actual_intoContribution == caseassert["actual_intoContribution"]
            log.error("U币贡献榜-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("U币贡献榜-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('我的守护页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoGuardian(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-我的守护-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoGuardian = my_page.intoGuardian()
        try:
            assert actual_intoGuardian == caseassert["actual_intoGuardian"]
            log.error("我的守护-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("我的守护-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('荣耀挑战赛页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoPkHistory(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-荣耀挑战赛-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoPkHistory = my_page.intoPkHistory()
        try:
            assert actual_intoPkHistory == caseassert["actual_intoPkHistory"]
            log.error("荣耀挑战赛-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("荣耀挑战赛-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('谁看过我页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoFootPrint(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-谁看过我-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoFootPrint = my_page.intoFootPrint()
        try:
            assert actual_intoFootPrint == caseassert["actual_intoFootPrint"]
            log.error("谁看过我-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("谁看过我-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('我看过的页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoWatchHistory(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-我看过的-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoWatchHistory = my_page.intoWatchHistory()
        with allure.step('我看过的页用例'):
            try:
                assert actual_intoWatchHistory == caseassert["actual_intoWatchHistory"]
                log.error("我看过的-测试用例通过")
            except AssertionError as a:
                log.error("断言失败")
                my_page.save_webImgs("我看过的-断言-截图")
                raise a
            my_page.back()

    @allure.story('我的')
    @allure.title('官方客服页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoackRL(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-官方客服-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoackRL = my_page.intoackRL()
        try:
            assert actual_intoackRL == caseassert["actual_intoackRL"]
            log.error("官方客服-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("官方客服-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('帮助中心页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoHelpCenter(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-帮助中心-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoHelpCenter = my_page.intoHelpCenter()
        try:
            assert actual_intoHelpCenter == caseassert["actual_intoHelpCenter"]
            log.error("帮助中心-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("帮助中心-断言-截图")
            raise a
        my_page.back()

    @allure.story('我的')
    @allure.title('联系我们页用例')
    @pytest.mark.parametrize("caseassert", myassert)
    def test_intoContactUs(self, caseassert, startApp_keepUserData1):
        log.info("*************************************我的-联系我们-测试用例******************************************")
        my_page = MyPage(startApp_keepUserData1)
        my_page.back()
        actual_intoContactUs = my_page.intoContactUs()
        try:
            assert actual_intoContactUs == caseassert["actual_intoContactUs"]
            log.error("联系我们-测试用例通过")
        except AssertionError as a:
            log.error("断言失败")
            my_page.save_webImgs("联系我们-断言-截图")
            raise a
        my_page.back()


if __name__ == '__main__':
    pytest.main()
