# coding:utf-8
from datetime import datetime
import json
import hashlib

class Util:

    @staticmethod
    def get_now_time():
        date = datetime.now()
        date = str(date)
        date = date[0:19]
        return date

    @staticmethod
    def json_out(out):
        return json.dumps(out, ensure_ascii=False)

    @staticmethod
    def md5(str):
        h1 = hashlib.md5()
        h1.update(str.encode(encoding='utf-8'))
        return h1.hexdigest()
