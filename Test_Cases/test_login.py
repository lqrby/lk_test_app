import allure
import pytest
from Common.log import get_logger
from TestDatas.login import login_success, login_error, qq_login, wb_login, wx_login
from Pages.pageObjects.login_page import LoginPage

log = get_logger(logger_name="登录操作日志")


@pytest.mark.run(order=7)
@allure.feature('登录')
class Test_Login:
    """密码错误的测试用例(账号或密码错误)"""
    @pytest.mark.error
    @pytest.mark.parametrize("errorData", login_error)
    @allure.story('登录失败用例')
    @allure.title('登录失败用例')
    def test_error_login(self, errorData, start_app):
        log.info("*********登陆失败用例：错误的密码*********")
        '''操作步骤：
            1.启动app点击同意用户协议按钮
            2.点击手机号登录
            3.点击账号密码登录
            4.输入错误的手机号密码点击“登录”按钮
        '''
        login_page = LoginPage(start_app)
        
        actual = login_page.login_mobile_passWord(errorData["username"], errorData["password"])
        with allure.step("手机号密码登录测试用例"):
            try:
                assert actual == errorData["check"]
                log.info("手机号密码登录成功")
            except AssertionError as a:
                log.exception("断言失败")
                login_page.save_webImgs("登录success_断言失败截图")
                raise a


    '''正常登陆的测试用例--手机号密码登陆'''
    @pytest.mark.success
    @pytest.mark.parametrize("case", login_success)
    @allure.story('手机号和密码登录')
    @allure.title('手机号&密码登录')
    def test_success_mobilelogin(self, case, start_app):
        log.info("*********手机号和密码登陆用例：正常场景*********")
        '''操作步骤：
            1.启动app点击同意用户协议按钮
            2.点击手机号登录
            3.点击账号密码登录
            4.输入正确的手机号密码点击“登录”按钮
        '''
        login_page = LoginPage(start_app)
        loginStatus = login_page.login_mobile_passWord(case["username"], case["password"])
        '''异常处理，预期结果与实际结果做对比，如果断言正确pass、如果断言失败或查找元素失败，自动截图保存路径到Outputs / screenshots'''
        with allure.step("手机号密码登录测试用例"):
            try:
                assert loginStatus == case["check"]
                log.info("手机号密码登录成功")
            except AssertionError as a:
                log.exception("登录成功用例断言失败")
                login_page.save_webImgs("登录success_断言失败截图")
                raise a


    '''正常手机号验证码登陆的测试用例'''
    @pytest.mark.success
    @pytest.mark.parametrize("case", login_success)
    @allure.story('手机号验证码登陆')
    @allure.title('手机号验证码登陆')
    def test_success_phoneCode(self, case, start_app):
        log.info("*********手机号验证码登陆用例:正常场景*********")
        '''操作步骤：
            1.启动app点击同意用户协议按钮
            2.点击手机号登录
            3.输入正确的手机号点击“获取验证码”按钮
        '''
        login_page = LoginPage(start_app)
        loginStatus = login_page.login_phone_code(case["username"])
        '''异常处理，预期结果与实际结果做对比，如果断言正确pass、如果断言失败或查找元素失败，自动截图保存路径到Outputs / screenshots'''
        with allure.step("手机号密码登录测试用例"):
            try:
                assert loginStatus == case["check"]
                log.info("手机号密码登录成功")
            except AssertionError as a:
                log.exception("断言失败")
                login_page.save_webImgs("登录success_断言失败截图")
                raise a



    # 微信登录
    @pytest.mark.parametrize("wx_case", wx_login)
    @allure.story('微信登录测试用例')
    @allure.title('微信登录测试用例')
    def test_success_weChatlogin(self, wx_case, start_app):
        log.info("*********微信登陆用例：正常场景*********")
        login_page = LoginPage(start_app)
        actual = login_page.login_byWechat_success(wx_case["wxName"],wx_case["wxPassword"])
        with allure.step("微信登录测试用例"):
            try:
                assert actual == wx_case["check"]
                log.info("微信登录成功")
            except AssertionError as a:
                log.exception("微信断言失败")
                login_page.save_webImgs("微信登录success_断言")
                raise a

    # 微博登录
    @pytest.mark.parametrize("wb_case", wb_login)
    @allure.story('微博登录测试用例')
    @allure.title('微博登录测试用例')
    def test_success_weChatlogin(self, wb_case, start_app):
        log.info("*********微博登陆用例：正常场景*********")
        login_page = LoginPage(start_app)
        actual = login_page.login_byWeiBo_success(wb_case["wbName"],wb_case["wbPassword"])
        with allure.step("微博登录测试用例"):
            try:
                assert actual == wb_case["check"]
                log.info("微博登录成功")
            except AssertionError as a:
                log.exception("微博断言失败")
                login_page.save_webImgs("微博登录success_断言")
                raise a

    # QQ登录
    @pytest.mark.parametrize("qq_case", qq_login)
    @allure.story('QQ登录测试用例')
    @allure.title('QQ登录测试用例')
    def test_success_QQlogin(self, qq_case, start_app):
        log.info("*********QQ登陆用例：正常场景*********")
        login_page = LoginPage(start_app)
        actual = login_page.login_byQQ_success(qq_case["qqName"],qq_case["qqPassword"])
        with allure.step("QQ登录测试用例"):
            try:
                assert actual == True
                log.info("QQ登录断言成功")
            except AssertionError as a:
                log.exception("qq登录断言失败")
                login_page.save_webImgs("qq登录success_断言")
                raise a

    


if __name__ == '__main__':
    pytest.main()
