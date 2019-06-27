__author__ = "luo"

import ddt
from ..common.data_excel import *
from ..common.public_class import *

# 测试数据
test_data = get_data_all(excel_name="faxian", sheet_name="faxian")


@ddt.ddt
class FaXianTest(SetupTeardown):
    """
    测试发现
    """
    @ddt.data(*get_data_by_key(data_all=test_data, url_key="foundGoodslist"))
    def test_found_goods(self, excel_data):
        """
        测试找货
        :param excel_data:
        """
        if excel_data:
            url = con.get_config("interface_api", "foundGoodslist")
            headers = {
                "token": token
            }
            result = UrlRequest.url_request(method=excel_data["method"],
                                            url=url,
                                            data=excel_data["params"],
                                            headers=headers)
            if result["msg"]:
                logger.critical(msg=u"config请求失败，请检查接口")
                sys.exit()
            self.assertFalse(result["msg"])
            self.assertEqual(result["result"]["success"], excel_data["success"])
        else:
            logger.warning(msg=u"未找到对应的url_key")

    @ddt.data(*get_data_by_key(data_all=test_data, url_key="saveFoundGood"))
    def test_release_goods(self, excel_data):
        """
        测试发布找货
        :return:
        """
        if excel_data:
            url = con.get_config("interface_api", "saveFoundGood")
            headers = {
                "token": token
            }
            result = UrlRequest.url_request(method=excel_data["method"],
                                            url=url,
                                            json=excel_data["params"],
                                            headers=headers)
            if result["msg"]:
                logger.critical(msg=u"config请求失败，请检查接口")
                sys.exit()
            self.assertFalse(result["msg"])
            self.assertEqual(result["result"]["success"], excel_data["success"])
        else:
            logger.warning(msg=u"未找到对应的url_key")





