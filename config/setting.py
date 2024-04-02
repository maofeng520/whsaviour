import os
import time

import pytest

# 获取本模块的上一个路径
BASE_PATH = os.path.dirname(os.path.dirname(__file__))  # E/Test_WeiHong

# 获取excel测试用例
excel_test_case = os.path.join(BASE_PATH + os.sep + 'testdata' + os.sep + 'excel' + os.sep + 'test_login.xlsx')

# 获取yaml测试用例
yaml_test_case = os.path.join(BASE_PATH + os.sep + 'testdata' + os.sep + 'yaml' + os.sep + 'login.yml')

# 获取log名称和路径
log_config = {'log_file_name': '%Y-%m-%d - %H-%M'}
log_name = time.strftime(log_config['log_file_name'])
path = os.path.dirname(os.path.dirname(__file__)) + os.sep + "test_result" + os.sep + 'log' + os.sep
log_path = path + log_name + '.log'

# 测试报告的路径
report_path = BASE_PATH + os.sep + 'report' + os.sep + 'report.html'

# 数据库配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '362046',
    'database': 'mysql',
    'port': 3306,
    'charset': 'utf8'
}



def get_path():
    print('主目录：{}'.format(BASE_PATH))
    print('excel全路径：{}'.format(excel_test_case))
    print('log全路径：{}'.format(log_path))
    print('测试报告路径：{}'.format(report_path))


class DynamicParam:
    pass


if __name__ == '__main__':
    get_path()
