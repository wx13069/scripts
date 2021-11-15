import json
import requests
from environs import Env

env = Env()
jhmck = env.list('jhmck')

cookie = jhmck
list(cookie)
i = len(cookie)

def qd():
    a = 0
    while a < i:
        ck = cookie[a]
#        print(ck)

        header = {
        'Host': 'txcs200.m.yunhuiyuan.cn',
        'Content-Length': '2',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3141 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/2741 MicroMessenger/8.0.10.1960(0x28000A3D) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
        'Cookie': ck
    }
        data = {}
        data = json.dumps(data)
        r = requests.post('https://txcs200.m.yunhuiyuan.cn/Member/Sign?bid=c59a6675-ff4e-45ba-bae7-6a3614efb769',headers=header, data=data)
        print('执行第'+a+1+'个账号签到')
        print(r.json())
        print('------------------------------------')
        a = a + 1
qd()


