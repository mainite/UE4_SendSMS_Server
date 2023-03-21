# _*_ coding: utf-8 _*_
"""
Time:     2020-07-05
Author:   inite.cn
File:     SendSMS.py
Describe: Use SMS messages to verify user's identity from Unreal,
marketplace link: https://www.unrealengine.com/marketplace/zh-CN/product/phoneauthcode
"""

import json,random,flask
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

# 生成验证码的长度
VerificationLen = 4

def BeginSend(PhoneNum,AccessKeyId,AccessSecret,SignName,TemplateCode):

    client = AcsClient(AccessKeyId, AccessSecret, 'cn-hangzhou')
    # 生成验证码
    authCode = str(random.randint(1000, (10**VerificationLen-1)))
    dict = {'code': authCode}
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')
    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', PhoneNum)
    request.add_query_param('SignName', SignName)
    request.add_query_param('TemplateCode', TemplateCode)
    # request.add_query_param('TemplateParam', "{'code':'5648'}")
    request.add_query_param('TemplateParam', str(dict))
    # 请求
    response = client.do_action(request)
    cjson = json.loads(str(response,'utf-8'))
    cjson['authCode'] = authCode
    print(json.dumps(cjson))
    return cjson

# 使用本文件作为服务名
server = flask.Flask(__name__)
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式


# 发送短信验证码
@server.route("/SendM", methods=['post'])
def SendM():
    cjson = flask.request.get_json()
    PhoneNum = cjson['PhoneNum']
    AccessKeyId = cjson['AccessKeyId']
    AccessSecret = cjson['AccessSecret']
    SignName = cjson['SignName']
    TemplateCode = cjson['TemplateCode']
    resu = BeginSend(PhoneNum,AccessKeyId,AccessSecret,SignName,TemplateCode)
    return resu



if __name__ == '__main__':

    server.run(debug=True, port=1234, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
