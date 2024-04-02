import datetime
import pytest
from utils.logger import logger
from config.setting import DynamicParam
import common.base as Base
import json
from utils.red_mysql import red_mysql_testcase
from utils.requests_utils import send_requests

attribute = DynamicParam()

# case_list = red_mysql_testcase.load_run_testcase('急救云')

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    pass
