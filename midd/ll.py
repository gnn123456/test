from common import confin
from logs.log import get_logger
from reports.request_1 import Request
import jsonpath
from reports.jm import decrypt_str
import json
from reports.parameter import data_1
from reports.methods import MD5Test
from common.splicing import conf_dir

def login():
    url="/member/login"
    method="post"
    data={"Mobile":"18735571533","Password":MD5Test("123123gnn").upper(),"deviceid":"123"}
    data_2 = data_1.data1
    data_2["data"] = data
    res=Request().request(method=method,url=url,json=data_2)
    return  json.loads(decrypt_str(res.json()))

def token_1():
    return jsonpath.jsonpath(login(),"$..Token")[0]








