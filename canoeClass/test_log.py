# -*-coding: "utf-8"-*-

"""
# File:        test_log.py
# Author:      "liyi"
# CreateTime:  2022/6/23 10:11
# Version:     python 3.6
# Description:   
"""
import datetime
import logging
import os

# class ConsolePanelHandler(logging.Handler):
#
#     def __init__(self, parent):
#         logging.Handler.__init__(self)
#         self.parent = parent
#
#     def emit(self, record):
#         """输出格式可以按照自己的意思定义HTML格式"""
#         record_dict = record.__dict__
#         asctime = record_dict['asctime'] + " >> "
#         line = record_dict['filename'] + " -> line:" + str(record_dict['lineno']) + " | "
#         levelname = record_dict['levelname']
#         message = record_dict['message']
#         if levelname == 'ERROR':
#             color = "#FF0000"
#         elif levelname == 'WARNING':
#             color = "#FFD700"
#         else:
#             color = "#008000"
#         html = f'''
#         <div >
#             <span>{asctime}</span>
#             <span style="color:#4e4848;">{line.upper()}</span>
#             <span style="color: {color};">{levelname}</span>
#             <span style="color:	#696969;">{message}</span>
#         </div>
#         '''
#         self.parent.write(html)  # 将日志信息传给父类 write 函数 需要在父类定义一个函数

class Log:
    def __init__(self, filename):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=20)

        now = datetime.datetime.now()  # 获取当前时间
        otherStyleTime = now.strftime("%Y-%m-%d")  # "%Y-%m-%d-%H-%M-%S"
        user_path = f"{os.getcwd()}\\logs"  # 获取用户路径
        os.makedirs(user_path, exist_ok=True)  # 获取用户 logs 文件夹  如果不存在则创建文件夹
        log_path = f"{user_path}\\{filename}_{otherStyleTime}.html"  # 以当前日期创建.log日志

        file_log = logging.FileHandler(log_path, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s >> (%(filename)s[line:%(lineno)d]) | %(levelname)s: %(message)s - ',
                                      '%Y-%m-%d %H:%M:%S')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def get_log(self):
        return self.logger