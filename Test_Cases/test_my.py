
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
            log.info("资料编辑页测试用例-测试用例通过")
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
            log.info("我的好友、谁看过我和派对足迹测试用例-测试用例通过")
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
            log.info("我的背包测试用例-测试用例通过")
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
            log.info("我的奖励中心测试用例-测试用例通过")
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
            log.info("活动中心测试用例-测试用例通过")
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
            log.info("申请家族测试用例-测试用例通过")
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
            log.info("设置-账号安全测试用例-测试用例通过")
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
            log.info("设置-未成年保护模式试用例-测试用例通过")
        except AssertionError as a:
            log.error("设置-未成年保护模式测试用例断言失败")
            raise


    @pytest.mark.success
    @allure.story('我的')
    @allure.title('设置》我的动态测试用例')
    def test_myDynamic(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>设置-我的动态测试用例***************")
        actual_edit = my_page.my_dynamic()
        try:
            assert actual_edit == True
            log.info("设置-我的动态试用例-测试用例通过")
        except AssertionError as a:
            log.error("设置-我的动态测试用例断言失败")
            raise
            
    @pytest.mark.success
    @allure.story('我的')
    @allure.title('设置》关于哩咔测试用例')
    def test_myLevel(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>设置-关于哩咔测试用例***************")
        actual_edit = my_page.about_lika()
        try:
            assert actual_edit == True
            log.info("设置-关于哩咔测试用例通过")
        except AssertionError as a:
            log.error("设置-关于哩咔测试用例断言失败")
            raise

    @pytest.mark.success
    @allure.story('我的')
    @allure.title('商城')
    def test_shopping_mall(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>商城测试用例***************")
        shopping_mall = my_page.shopping_mall()
        try:
            assert shopping_mall == True
            log.info("商城测试用例通过")
        except AssertionError as a:
            log.error("商城测试用例断言失败")
            raise
            
    

    @pytest.mark.success
    @allure.story('我的')
    @allure.title('收入')
    def test_income(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>收入测试用例***************")
        income = my_page.income()
        try:
            assert income == True
            log.info("收入测试用例通过")
        except AssertionError as a:
            log.error("收入测试用例断言失败")
            raise


    @pytest.mark.success
    @allure.story('我的')
    @allure.title('会员')
    def test_member(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>会员测试用例***************")
        member = my_page.member()
        try:
            assert member == True
            log.info("会员测试用例通过")
        except AssertionError as a:
            log.error("会员测试用例断言失败")
            raise
            
    @pytest.mark.success
    @allure.story('我的')
    @allure.title('充值')
    def test_recharge(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>充值测试用例***************")
        recharge = my_page.recharge()
        try:
            assert recharge == True
            log.info("充值测试用例通过")
        except AssertionError as a:
            log.error("充值测试用例断言失败")
            raise
            
    @pytest.mark.success
    @allure.story('我的')
    @allure.title('等级')
    def test_mylevel(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>等级测试用例***************")
        my_level = my_page.my_level()
        try:
            assert my_level == True
            log.info("等级测试用例通过")
        except AssertionError as a:
            log.error("等级测试用例断言失败")
            raise
            

    

# if __name__ == '__main__':
#     pytest.main()
