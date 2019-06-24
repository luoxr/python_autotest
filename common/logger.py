__author__ = "luo"

import logging
import os
import time
import sys
from colorama import Fore, Style


class Logger(object):

    def __init__(self, logger):
        """
        生成日志
        :param logger: 定义对应的程序模块名name，默认为root
        """
        # 创建一个logger
        self.logger = logging.getLogger(name=logger)
        # 指定最低的日志级别 critical > error > warning > info > debug
        self.logger.setLevel(logging.DEBUG)
        # 设置日志格式
        fmt = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        file_format = logging.Formatter(fmt=fmt)
        # 设置日志路径
        rq = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
        log_path = os.getcwd() + "/logs/"
        log_name = log_path + rq + ".log"
        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志，解决重复打印的问题
        if not self.logger.handlers:

            # 创建一个handler，写入日志
            file_handler = logging.FileHandler(log_name, encoding="utf-8")
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(file_format)

            # 再创建一个handler，用于输出到控制台
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(file_format)

            # 给logger添加handler
            self.logger.addHandler(hdlr=file_handler)
            self.logger.addHandler(hdlr=console_handler)

    def debug(self, msg):
        """
        定义输出到控制台的颜色debug--white，info--blue，warning--yellow, error/critical--red
        :param msg: 输出的log文字
        :return:
        """
        self.logger.debug(Fore.WHITE + str(msg) + Style.RESET_ALL)

    def info(self, msg):
        self.logger.info(Fore.BLUE + str(msg) + Style.RESET_ALL)

    def warning(self, msg):
        self.logger.warning(Fore.YELLOW + str(msg) + Style.RESET_ALL)

    def error(self, msg):
        self.logger.error(Fore.RED + str(msg) + Style.RESET_ALL)

    def critical(self, msg):
        self.logger.critical(Fore.RED + str(msg) + Style.RESET_ALL)



