import pymysql
from config.setting import db_config
from utils.logger import logger


class DB:
    def __init__(self):
        self.conn = pymysql.connect(**db_config, autocommit=True)
        # 以字典形式返回操作结果
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def select_fetchone(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        logger.info('数据库查询结果为：{}'.format(res))
        return res

    def select_fetchall(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        # logger.info('数据库查询结果为：{}'.format(res))
        return res

    def execute_db(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            logger.info('执行sql语句成功！')
        except Exception as e:
            logger.info(sql)
            logger.error('执行sql语句出错了，错误原因为:{}'.format(e))
            self.conn.rollback()
            return False

    def __del__(self):
        self.cursor.close()
        self.conn.close()


db = DB()

if __name__ == '__main__':
    # pass
    DB().select_fetchall('select * from test_user')
