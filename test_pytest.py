import pytest
import json


def test_json():
    num = json.dumps("false", ensure_ascii=False)
    print('结果为:{}'.format(num))

