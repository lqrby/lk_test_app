import pytest
from Common.log import get_logger
from TsetDatas.login import login_phone, login_error
from Pages.iOS_pageObjects.login_page import LoginPage
from Pages.iOS_pageObjects.env_page import EnvPage
from Pages.iOS_pageObjects.common_buss import CommonBus

log = get_logger(logger_name="登录操作日志")

@pytest.mark.run(order=1)
class Test_Login:
    """正常登陆的测试用例--手机号登陆"""
    @pytest.mark.success
    @pytest.mark.parametrize("case", login_phone)
    def test_phone_login(self, case, start_iOS):
        log.info("*********登陆用例：正常场景*********")
        '''登录之后点击首页的："登录另一个账号"按钮'''
        # CommonBus(start_iOS).switch_navigate("登录另一个账号")
        '''操作步骤：
            环境初始化
            1.选择登录方式
            2.点击手机号登录
            3.输入正确的手机号点击“确定”按钮
            4.输入正确的密码点击"确定"按钮
            5.关闭首页广告
            6.关闭首页弹框
            7.获取首页title"Uplive"做正确的断言'''
        env = EnvPage(start_iOS)
        env.env_change("stage")

        login_page = LoginPage(start_iOS)
        login_page.login_check()
        actual = login_page.login_iOS_phone(case["username"], case["password"])
        '''异常处理，预期结果与实际结果做对比，如果断言正确pass、如果断言失败或查找元素失败，自动截图保存路径到Outputs / screenshots'''
        try:
            assert actual == case["check"]
            log.info("登录成功")
        except AssertionError as a:
            log.exception("断言失败")
            login_page.save_webImgs("登录success_断言")
            raise a
        CommonBus(start_iOS).quit_login()


if __name__ == '__main__':
    pytest.main()
