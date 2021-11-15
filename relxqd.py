import requests
import json
url ='https://app.relxtech.com/dianziyan-api/api/clock-in'
heards ={
'token':'4c1cd5917de148f1adb78fa6d211ba6b',
'Content-Type':'application/json; charset=utf-8',
'host':'app.relxtech.com',
'Content-Length':'10',
}

r = requests.post(url=url,data=json.dumps({"type":1}),headers=heards)
print(r.text)

url = 'https://app.relxtech.com/api/crm/scan/record/v2'
##data =
heards = {
    "Host":"app.relxtech.com",
    "Content-Length":"102",
    "Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNzAyNzA2NCIsImlhdCI6MTYzNDQ3MTkyNiwic3ViIjoie1wic2Vzc2lvbklkXCI6XCIxNzAyNzA2NFwiLFwidXNlcklkXCI6MTcwMjcwNjQsXCJjb2RlXCI6XCIyMDIxMTAwNzE1NDc1NDIzNzgyXCIsXCJjZWxscGhvbmVcIjpcIjE3NioqKio2NjgyXCIsXCJpZGVudGl0eUF1dGhlbnRpY2F0aW9uU3RhdHVzXCI6MSxcInJlZ2lzdGVyQ2hhbm5lbFwiOlwiMTVcIixcInBvc3BhbFVzZXJJZFwiOjgyODMyNTUzMzI5NDg1NDg0OSxcIm5hbWVcIjpcIuWtkOmdnumxvFwiLFwiYWNjb3VudFR5cGVcIjpcIkNVU1RPTUVSX1VTRVJcIixcImhhc2hDcFwiOlwiMGVCbDJ5cEFWMkJFZzUxcVwiLFwiZmFjZUlkZW50aXR5U3RhdHVzXCI6MH0iLCJleHAiOjE2MzcwNjM5MjZ9.TShHqIxKKtLXAu5uo8v6VIlOjvwS6ig9Bqz_c5FE_V8",
    "User-Agent":"Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3135 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/1819 MicroMessenger/8.0.10.1960(0x28000A3D) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "sentry-trace":"9993fd84f79e41beaa87105a6fc957eb-86ed2e34cc9aef32-1",
    "Content-Type":"application/json;charset=UTF-8",
    "Cookie":"acw_tc=2760824f16344719265441725e942aaf066927099fa3634cf12741c8a85e95; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217c8e1e6008189-07a60801af8344-50645f14-334443-17c8e1e60093e7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217c8e1e6008189-07a60801af8344-50645f14-334443-17c8e1e60093e7%22%7D; token=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNzAyNzA2NCIsImlhdCI6MTYzNDQ3MTkyNiwic3ViIjoie1wic2Vzc2lvbklkXCI6XCIxNzAyNzA2NFwiLFwidXNlcklkXCI6MTcwMjcwNjQsXCJjb2RlXCI6XCIyMDIxMTAwNzE1NDc1NDIzNzgyXCIsXCJjZWxscGhvbmVcIjpcIjE3NioqKio2NjgyXCIsXCJpZGVudGl0eUF1dGhlbnRpY2F0aW9uU3RhdHVzXCI6MSxcInJlZ2lzdGVyQ2hhbm5lbFwiOlwiMTVcIixcInBvc3BhbFVzZXJJZFwiOjgyODMyNTUzMzI5NDg1NDg0OSxcIm5hbWVcIjpcIuWtkOmdnumxvFwiLFwiYWNjb3VudFR5cGVcIjpcIkNVU1RPTUVSX1VTRVJcIixcImhhc2hDcFwiOlwiMGVCbDJ5cEFWMkJFZzUxcVwiLFwiZmFjZUlkZW50aXR5U3RhdHVzXCI6MH0iLCJleHAiOjE2MzcwNjM5MjZ9.TShHqIxKKtLXAu5uo8v6VIlOjvwS6ig9Bqz_c5FE_V8",

}
r = requests.post(url=url,data=json.dumps( {
    "clientType":"CRM",
    "fullUrl":"https://crm.relxtech.com/api/s?c=98SQINOE5D232A",
    "scanClient":"wechat"
}),headers=heards)
print(r.status_code)
if (r.status_code == 200):
    print('微信端扫码打卡成功')
else:
    print('微信端打卡失败')
