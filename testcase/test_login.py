import ast
import json

import requests
import pytest
from utils.logger import logger
import os
from utils.excel_util import read_excel
from config.setting import excel_test_case
from utils.requests_utils import send_requests
from utils.red_mysql import red_mysql_testcase
import datetime
from common import base
from config.setting import DynamicParam

mysql_data = red_mysql_testcase.load_run_testcase('急救云')

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

attribute = DynamicParam()


class TestLogin:
    def setup_class(self):
        logger.info('------开始执行测试用例，开始时间为：{}------'.format(current_time))

    def teardown_class(self):
        logger.info('------执行测试结束，完成时间为：{}------'.format(current_time))

    # 根据关联，获取该变量内容
    def correlation(self, data):
        res_data = base.find(data)
        if res_data:
            replace_dict = {}
            for i in res_data:
                data_tmp = getattr(DynamicParam, str(i), "None")
                replace_dict.update({str(i): data_tmp})
            data = json.loads(base.relace(data, replace_dict))
        return data

    # 响应结果关联设置函数
    def set_relation(self, relation, res_data):
        try:
            if relation:
                relation = relation.split(",")
                for i in relation:
                    var = i.split("=")
                    var_name = var[0]
                    var_tmp = var[1].split(".")
                    res = base.parse_relation(var_tmp, res_data)
                    print("{}={}".format(var_name, res))
                    setattr(DynamicParam, var_name, res)
        except Exception as e:
            print(e)

    @pytest.mark.parametrize('case', mysql_data)
    def test_login(self, case):
        res_data = None
        url = red_mysql_testcase.load_config('急救云', 'url_api')['value'] + case['url']
        method = case['method']
        headers = json.loads(case['headers'])
        data = json.loads(case['request_body'])
        token = case['token']
        relation = case['relation']
        case_name = case['title']

        headers = self.correlation(headers)
        token = self.correlation(token)
        data = self.correlation(data)
        try:
            logger.info("***正在执行{}用例***".format(case_name))
            res_data = send_requests.api_run(url=url, method=method, headers=headers, data=data)
            logger.info("用例执行成功，请求的结果为：{}".format(res_data))
        except:
            logger.info("用例执行失败，请查看日志找原因。")
            assert False
        if res_data:
            if relation != "None":
                self.set_relation(relation, res_data)
        self.assert_respose(case, res_data)
        return res_data

    # 结果验证方法
    def assert_respose(self, case, res_data):
        is_pass = False
        try:
            assert res_data['success'] == ast.literal_eval(case['expected_code'])
            logger.info('用例断言成功')
            is_pass = True
        except:
            is_pass = False
            logger.info("用例断言失败")
        finally:
            red_mysql_testcase.insert_testresults(res_data, is_pass, str(case['id']))
            assert is_pass
        return is_pass


if __name__ == '__main__':
    pytest.main(['test_login.py', '-v', '-s'])
