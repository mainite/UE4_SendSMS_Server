# UE4_SendSMS_Server
Use SMS messages to verify user's identity


### Links:

marketplace:https://www.unrealengine.com/marketplace/en-US/product/phoneauthcode

documentation：https://inite.blog.csdn.net/article/details/107199014



### Python：

```shell
python -m pip install --upgrade pip
pip3 install flask
pip3 install aliyun-python-sdk-core 
pip3 install aliyun-python-sdk-ecs 
nohup python3 SendSMS.py >> ./log.SendSMS 2>&1 &
```


### Docker：

```shell
docker run inittt/ue4_send_sms
```
