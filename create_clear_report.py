__author__ = "luo"

import shutil
import os


class DeleteFiles(object):
    """
    删除指定目录下有的文件和文件夹
    :param path_dir 文件名
    """
    def __init__(self, path_dir):
        self.path_dir = path_dir

    def delete_files(self):
        # 获取指定文件路径，os.getcwd() 查看当前工作目录
        file_dir = os.getcwd() + self.path_dir

        # listdir(path)返回path指定的文件夹包含的文件或文件夹的名字的列表
        file_list = list(os.listdir(file_dir))

        # 遍历文件名列表，将文件名替换为路径
        for i in range(0, len(file_list)):
            file_list[i] = file_dir + file_list[i]

        # 遍历路径列表
        for file in file_list:
            if os.path.isfile(file):   # 判断路径是否为文件
                os.remove(file)
            else:
                shutil.rmtree(file)  # shutil.rmtree()删除非空目录; os.rmdir()删除空目录


def clear_report_files():
    dir_list = ["\\report\\", "\\logs\\"]
    file_dir = os.getcwd()
    for i in range(0, len(dir_list)):
        DeleteFiles(path_dir=dir_list[i]).delete_files()
        print("清除目录%s%s成功！" % (file_dir, dir_list[i]))


def create_report_dirs():
    """
    创建存放report、logs两个文件夹，如已有则不创建
    """
    dir_name_list = ["report", "logs"]
    file_dir = os.getcwd()
    for i in range(len(dir_name_list)):
        path = file_dir + "\\" + dir_name_list[i]
        # 不存在此目录才创建
        if not os.path.exists(path):
            os.makedirs(path)
            print("创建目录%s成功" % path)
        else:
            print("目录%s已存在，未进行创建" % path)


