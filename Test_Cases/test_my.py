
import allure
import pytest
from Pages.pageObjects.my_page import MyPage
from TestDatas.my import profileData
from Common.log import get_logger

log = get_logger(logger_name="我的操作日志")

'''我的页面'''


@pytest.mark.run(order=4)
@allure.feature('我的')
class Test_my:
    
    @allure.story('我的')
    @allure.title('查看个人资料用例')
    def test_viewMyProfile(self, startApp_keepUserData):
        log.info("**************我的-查看个人资料-测试用例**************")
        my_page = MyPage(startApp_keepUserData)
        myprofile = my_page.view_my_profile()
        try:
            assert myprofile == True
            log.info("查看个人资料-测试用例通过")
        except AssertionError as a:
            log.error("查看个人资料-断言失败")
            raise

            
    @pytest.mark.success
    @allure.story('我的')
    @allure.title('编辑页用例')
    @pytest.mark.parametrize("myProfileData", profileData)
    def test_editMyProfile(self,myProfileData, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的-资料编辑页-测试用例***************")
        actual_edit = my_page.edit_my_profile(myProfileData)
        try:
            assert actual_edit == True
            log.error("资料编辑页测试用例-测试用例通过")
        except AssertionError as a:
            log.error("资料编辑页断言失败")
            raise



    @pytest.mark.success
    @allure.story('我的')
    @allure.title('我的好友、谁看过我和派对足迹用例')
    def test_myFriendWhoLookMePartyFootprints(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>我的好友、谁看过我和派对足迹-测试用例***************")
        actual_edit = my_page.myFriend_whoLookMe_partyFootprints()
        try:
            assert actual_edit == True
            log.error("我的好友、谁看过我和派对足迹测试用例-测试用例通过")
        except AssertionError as a:
            log.error("我的好友、谁看过我和派对足迹测试用例断言失败")
            raise


    @pytest.mark.success
    @allure.story('我的')
    @allure.title('我的背包用例')
    def test_myKnapsack(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>我的背包-测试用例***************")
        actual_edit = my_page.my_knapsack()
        try:
            assert actual_edit == True
            log.error("我的背包测试用例-测试用例通过")
        except AssertionError as a:
            log.error("我的背包测试用例断言失败")
            raise
            
    @pytest.mark.success
    @allure.story('我的')
    @allure.title('我的奖励中心用例')
    def test_rewardCenter(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>我的奖励中心-测试用例***************")
        actual_edit = my_page.reward_center()
        try:
            assert actual_edit == True
            log.error("我的奖励中心测试用例-测试用例通过")
        except AssertionError as a:
            log.error("我的奖励中心测试用例断言失败")
            raise


    @pytest.mark.success
    @allure.story('我的')
    @allure.title('活动中心用例')
    def test_activityCenter(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>活动中心-测试用例***************")
        actual_edit = my_page.activity_center()
        try:
            assert actual_edit == True
            log.error("活动中心测试用例-测试用例通过")
        except AssertionError as a:
            log.error("活动中心测试用例断言失败")
            raise


    @pytest.mark.success
    @allure.story('我的')
    @allure.title('申请家族用例')
    def test_applicationFamily(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>申请家族-测试用例***************")
        actual_edit = my_page.application_family()
        try:
            assert actual_edit == True
            log.error("申请家族测试用例-测试用例通过")
        except AssertionError as a:
            log.error("申请家族测试用例断言失败")
            raise


    @pytest.mark.success
    @allure.story('我的')
    @allure.title('设置》账号安全用例')
    def test_accountSecurity(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>设置-账号安全测试用例***************")
        actual_edit = my_page.account_security()
        try:
            assert actual_edit == True
            log.error("设置-账号安全测试用例-测试用例通过")
        except AssertionError as a:
            log.error("设置-账号安全测试用例断言失败")
            raise
            

    
    @pytest.mark.success
    @allure.story('我的')
    @allure.title('设置》未成年保护模式用例')
    def test_protectionOfMinors(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>设置-未成年保护模式测试用例***************")
        actual_edit = my_page.protection_of_minors()
        try:
            assert actual_edit == True
            log.error("设置-未成年保护模式试用例-测试用例通过")
        except AssertionError as a:
            log.error("设置-未成年保护模式测试用例断言失败")
            raise
            

    

if __name__ == '__main__':
    pytest.main()
