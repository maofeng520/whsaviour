import json

import pytest
from utils.logger import logger
from utils.mysql import db
import datetime


class Red_Mysql_Testcase:

    # 加载所有的测试用例
    def load_all_testcase(self, web):
        db.select_fetchall('select * from test_case where web="{}"'.format(web))
        # db.select_fetchall("select * from test_case where web='急救云'")

    # 加载可执行的测试用例
    def load_run_testcase(self, web):
        run_list = db.select_fetchall('select * from test_case_copy where web="{}" and isdel=1'.format(web))
        # logger.info("可执行的测试用例：{}".format(run_list))
        return run_list

    # 查询配置信息
    def load_config(self, web, key):
        config = db.select_fetchone('select * from test_config where web="{}" and `key`="{}"'.format(web, key))
        return config

    # 新增测试结果
    def insert_testresults(self, response, is_pass, case_id):
        # 获取当前时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # response = json.dumps(response, ensure_ascii=False)
        sql = ('insert into test_result_record(`case_id`, `times`, `response`, `result`) values ("{}", "{}", "{}", '
               '"{}") '.format(case_id, now_time, response, is_pass))
        rows = db.execute_db(sql)
        return rows


red_mysql_testcase = Red_Mysql_Testcase()

if __name__ == '__main__':
    # mysql_config = red_mysql_testcase.load_config('急救云', 'url_api')
    # print(mysql_config)

    pass

    # mysql_case = red_mysql_testcase.load_run_testcase('急救云')
    # print(mysql_case)

    # insert_mysql = red_mysql_testcase.insert_testresults("<Response [200]>", "False", "1")
    # print(insert_mysql)
