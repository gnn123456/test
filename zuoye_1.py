import requests
# # 注册接口调用
data={"mobilephone":15003556788,"amount":"123456"}
resp=requests.get("http://test.lemonban.com/futureloan/mvc/api/member/withdraw",params=data)
# print("请求的地址:{}".format(resp.request.url))
# print("请求参数：{}".format(resp.request.body))
# print("请求头：{}".format(resp.request.headers))
# print("请求cookies：{}".format(resp.request._cookies))
# print("响应码：{}".format(resp.status_code))
print("响应信息为：{}".format(resp.json()))
# print("响应cookies：{}".format(resp.cookies))
# # 登录接口调用
# data={"mobilephone":"15711360090","pwd":"123123"}
# resp=requests.post("http://test.lemonban.com/futureloan/mvc/api/member/login",data=data)
# print("请求的地址:{}".format(resp.request.url))
# print("请求参数：{}".format(resp.request.body))
# print("请求头：{}".format(resp.request.headers))
# print("请求cookies：{}".format(resp.request._cookies))
# print("响应码：{}".format(resp.status_code))
# print("响应信息为：{}".format(resp.json()))
# print("响应cookies：{}".format(resp.cookies))
# # 充值接口的调用
# data_1={"mobilephone":15711360090,"amount":20.22}
# resp_1=requests.get("http://test.lemonban.com/futureloan/mvc/api/member/recharge",params=data_1,cookies=resp.cookies)
# # print("请求的地址:{}".format(resp_1.request.url))
# # print("请求参数：{}".format(resp_1.request.body))
# # print("请求头：{}".format(resp_1.request.headers))
# # print("请求cookies：{}".format(resp_1.request._cookies))
# # print("响应码：{}".format(resp_1.status_code))
# print("响应信息为：{}".format(resp_1.json()))
# print("响应信息为：{}".format(resp_1.json()["code"]))
# print("响应cookies：{}".format(resp_1.cookies))
# a = 1
# b = a
# a = 2
# print(b)

