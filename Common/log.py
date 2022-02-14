'''
Author: your name
Date: 2021-08-27 16:38:44
LastEditTime: 2021-08-27 16:40:07
LastEditors: your name
Description: In User Settings Edit
FilePath: /lk_test_app/Common/log.py
'''
import logging
import logging.handlers
from Common.splicing import reports_log


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)  # 创建一个自己得容器
    # logger.handlers.clear()
    if not logger.handlers:
        logger.setLevel("DEBUG")  # 给自己得容器设置级别
        #设置输出渠道
        #%(asctime)s  # 当前时间          
        # "[%(levelname)s]-"  # 当前级别
        #"%(filename)s-"  # 当前日志执行的模块名
        #"%(name)s-"  # 当前日志名
        #"日志信息:%(message)s")  # 日志信息
        formatter = logging.Formatter('%(asctime)s [%(levelname)s]%(filename)s[line:%(lineno)d] %(message)s')

        # 1设置一个输出到控制台得输出渠道，指定输出
        sc = logging.StreamHandler()
        sc.setLevel("DEBUG")
        sc.setFormatter(formatter)

        # 输出指定得级别到一个文件内
        file = logging.handlers.RotatingFileHandler(reports_log, encoding="UTF-8")
        file.setLevel("INFO")
        file.setFormatter(formatter)
        logger.addHandler(sc)
        logger.addHandler(file)

    return logger


if __name__ == "__main__":
    logging = get_logger(logger_name="任保玉")
    logging.error("this.is error")
