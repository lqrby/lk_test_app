
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


            
    @pytest.mark.success
    @allure.story('我的')
    @allure.title('我的动态用例')
    def test_intoEdit(self, startApp_keepUserData):
        my_page = MyPage(startApp_keepUserData)
        log.info("*************我的>我的动态-测试用例***************")
        actual_edit = my_page.my_dynamic()
        try:
            assert actual_edit == True
            log.error("我的动态测试用例-测试用例通过")
        except AssertionError as a:
            log.error("我的动态测试用例断言失败")
            

    

if __name__ == '__main__':
    pytest.main()
