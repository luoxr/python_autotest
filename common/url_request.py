__author__ = "luo"

import requests
from .logger import *

logger = Logger(logger="url_request")


class UrlRequest:

    @staticmethod
    def url_request(method, url, data=None, json=None, headers=None, cookies=None):
        r"""
        请求接口，返回响应数据

        :param method: method(get/post/put/delete)
        :param url: 请求的url
        :param data: 请求参数，字典形式
        :param json: 请求参数，json形式
        :param headers: headers，字典形式
        :param cookies: cookies
        :return: 返回result: {"result": result, "msg": msg}，字典形式
        """
        # 超时时间
        timeout = 10
        # 接口返回的数据(result:存放数据，msg:存放输出信息)
        result = {"result": None, "msg": None}

        try:
            if method == "get":
                response = requests.get(url=url, params=data, headers=headers, cookies=cookies, timeout=timeout)
                # 如果响应状态码不是 200，就主动抛出异常
                response.raise_for_status()
            elif method == "post":
                if data:
                    response = requests.post(url=url, data=data, headers=headers, cookies=cookies, timeout=timeout)
                    response.raise_for_status()
                else:
                    response = requests.post(url=url, json=json, headers=headers, cookies=cookies, timeout=timeout)
                    response.raise_for_status()
            elif method == "put":
                if data:
                    response = requests.put(url=url, data=data, headers=headers, cookies=cookies, timeout=timeout)
                    response.raise_for_status()
                else:
                    response = requests.put(url=url, json=json, headers=headers, cookies=cookies, timeout=timeout)
                    response.raise_for_status()
            elif method == "delete":
                if data:
                    response = requests.delete(url=url, data=data, headers=headers, cookies=cookies, timeout=timeout)
                    response.raise_for_status()
                else:
                    response = requests.delete(url=url, json=json, headers=headers, cookies=cookies, timeout=timeout)
                    response.raise_for_status()
            else:
                msg = "请求方式错误，请检查（get/post/put/delete）"
                result["msg"] = msg
                logger.error(msg=msg)
                return result
        # Requests显式抛出的异常都继承自 requests.exceptions.RequestException
        except requests.exceptions.RequestException as e:
            msg = "接口请求发生了异常：%s" % e
            logger.error(msg=msg)
            result["msg"] = msg
        # 在try子句没有发生任何异常、没有return语句的时候执行
        else:
            try:
                result["result"] = response.json()
            except requests.exceptions.RequestException:
                # 响应数据不为json格式
                result["result"] = response.text
        return result


