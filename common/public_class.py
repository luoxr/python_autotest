__author__ = "luo"

import unittest
from TestUnittest.common.data_config import *
from TestUnittest.common.url_request import *


class SetupTeardown(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("class module 开始测试>>>>>>>>>>>")

    @classmethod
    def tearDownClass(cls):
        print("class module 测试结束>>>>>>>>>>>>\n")

    def setUp(self):
        print("setup begin test")

    def tearDown(self):
        print("teardown test end!")


def get_user_info():
    """
    获取用户信息
    :return:
    """
    # 请求登录接口，获取token
    login_url = con.get_config("interface_api", "checkLogin")
    login_params = {
        "userName": con.get_config(section="login_config", key="username"),
        "password": con.get_config(section="login_config", key="password"),
        "sourceType": con.get_config(section="login_config", key="sourceType"),
        "type": con.get_config(section="login_config", key="type")
    }
    login_result = UrlRequest.url_request(method="post", url=login_url, json=login_params)
    if login_result["msg"]:
        logger.critical(msg="token请求失败，请检查接口！")
        sys.exit()
    token_ = login_result.get("result")["data"]["token"]

    # 请求用户信息接口，获取用户信息
    userinfo_url = con.get_config("interface_api", "getShopUserInfo")
    userinfo_params = {
        "token": token_
    }
    userinfo_result = UrlRequest.url_request(method="get", url=userinfo_url, data=userinfo_params)
    if userinfo_result["msg"]:
        logger.critical(msg="token无效，获取用户信息失败，请检查登录信息")
        sys.exit()
    userinfo_ = userinfo_result["result"]

    return [userinfo_, token_]


userinfo = get_user_info()
user_info = userinfo[0]
token = userinfo[1]

