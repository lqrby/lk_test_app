'''
Author: your name
Date: 2021-09-06 15:59:49
LastEditTime: 2021-09-18 13:26:53
LastEditors: your name
Description: In User Settings Edit
FilePath: /lk_test_app/Test_Cases/a_test_register.py
'''
import pytest
from Common.log import get_logger
from TestDatas.register import register_success
from Pages.pageObjects.Common_Buss import CommonBus as  Cb
from Pages.pageObjects.register_page import RegisterPage

log = get_logger(logger_name="注册操作日志")
from Pages.pageObjects.Common_Buss import CommonBus

'''需要确认注册之后的流程到底是什么'''


@pytest.mark.run(order=8)
class Test_Register:
    ''''''
    '''注册成功-手机号注册'''

    @pytest.mark.success
    @pytest.mark.parametrize("case", register_success)
    def test_success_register(self, case, start_app):
        log.info("*********登陆用例：注册场景*********")
        '''登录之后点击首页的："登录另一个账号"按钮'''
        # Cb(start_app).switch_navigate("登录另一个账号")

        '''操作步骤：
            1.点击...选择登录方式
            2.点击手机号登录
            3.随机输入手机号点击“确定”按钮
            4.输入正确的密码点击"确定"按钮
            5.个人资料-点击跳过
            6.获取首页title"Uplive"做正确的断言'''
        register_page = RegisterPage(start_app)

        actual = register_page.input_username(case["username"]).input_passwd(case["code"],
                                                                             case["password"]).register_title()
        try:
            assert actual == case["check1"] or actual == case["check2"]
            log.error("注册成功")
        except AssertionError as a:
            log.error("断言失败")
            register_page.save_webImgs("注册-断言-截图")
            raise a
        CommonBus(start_app).quit_login()


if __name__ == '__main__':
    pytest.main()
