__author__ = "luo"

import configparser
from .logger import *

logger = Logger(logger="data_config")


class Config(object):
    """
    读取config配置文件
    """
    def __init__(self):
        self.ini = configparser.ConfigParser()
        self.path = os.path.join(os.path.realpath(__file__).split("common")[0], "testData", "config.ini")

    def get_config(self, section, key=None):
        """
        获取config配置文件中的指定数据
        :param section: section
        :param key: 指定key
        :return: 返回list
        """
        self.ini.read(self.path, encoding="utf-8-sig")
        try:
            if key:
                config = self.ini.get(section, key)
            else:
                config = self.ini.items(section)
        except configparser.Error as msg:
            msg = u"读取配置文件错误，请检查输入，错误详情：" + str(msg)
            logger.error(msg=msg)
            config = False

        return config


con = Config()


