import requests
from utils.logger import logger


class Send_Requests:
    def api_run(self, url, method, headers=None, data=None):
        logger.info('发送请求的url为：{}'.format(url))
        logger.info('发送请求的method为：{}'.format(method))
        logger.info('发送请求的headers为：{}'.format(headers))
        logger.info('发送请求的data为：{}'.format(data))
        res = None
        if method.lower() == 'post':
            if headers == {"Content-Type": "application/json"}:
                res = requests.post(url=url, headers=headers, json=data)
            elif headers == {"Content-Type": "application/x-www-form-urlencoded"}:
                res = requests.post(url=url, headers=headers, data=data)
        elif method.lower() == 'get':
            res = requests.get(url=url, headers=headers, params=data)
        elif method.lower() == 'put':
            res = requests.put(url=url, headers=headers, json=data)
        elif method.lower() == 'delete':
            res = requests.delete(url=url, headers=headers, params=data)
        logger.info('响应状态码为：{}'.format(res.status_code))
        logger.info('响应success为：{}'.format(res.json()["success"]))
        logger.info('响应message为：{}'.format(res.json()["message"]))
        return res.json()


send_requests = Send_Requests()

if __name__ == '__main__':
    pass
    # url = 'http://systest.whsaviour.com/platform-admin/sys/login'
    # method = 'post'
    # headers = {"Content-Type": "application/json"}
    # data = {"username": "admin", "password": "10010.com"}
    # send_requests.api_run(url=url, method=method, headers=headers, data=data)

    # reqes = requests.post(url=url, headers=headers, json=data)
    # print(reqes.json())
