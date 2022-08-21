from datetime import datetime
import requests
import json


app_id = 'wx266a7570f0f5f03f'
app_secret = '1d181e1501f1b74cc0dcebef81414128'
template_id = '7WcvYmT44jwWUbAR0sXKSUzXIXfzrveZKREvO2KsdLA'

access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(app_id,app_secret)
res = requests.get(access_token_url).json()
access_token = res['access_token']
users = ['ozBHL59pCNzQaGm3zhapKlwVYAUc', 'ozBHL57VU9iTx4-c89Hq1JKk12Yw']


def weather():
    host = 'https://jisutqybmf.market.alicloudapi.com'
    path = '/weather/query'
    appcode = 'b4c8a39e21e5415caf458b5f3217d4c6'
    # querys = 'city=%E5%BB%89%E6%B1%9F'
    city = '佛山禅城区'

    url = host + path + '?' + 'city={}'.format(city)

    header = {"Authorization": "APPCODE b4c8a39e21e5415caf458b5f3217d4c6"}
    content = requests.get(url, headers=header)  # 返回状态码
    print(content)
    try:
        data = json.loads(content.text)  # 把json字符串转换为字典
    except ValueError:
        print("try again")
    else:
        result = data.get("result")
        city = result.get("city")
        date = result.get("date")
        week = result.get("week")
        weather = result.get("weather")  # 天气
        temp = result.get("temp")        # 气温
        temphigh = result.get("temphigh")
        templow = result.get("templow")

        now = datetime.strftime(datetime.today(), "%Y-%m-%d")
        data = {
            'date': {'value': now + ' ' + week},
            'city': {'value': city},
            'weather': {'value': weather, 'color': '#f51616'},
            'temp': {'value': temp + '°C'},
            'min_teamperature': {'value': templow + '°C'},
            'max_teamperature': {'value': temphigh + '°C' + '\n'},
            'msg': {'value': 'BlackPink girl 哈哈哈哈哈。。。', 'color': '#e06666'},
        }

        # 给用户天气消息
        push_url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
        for user_id in users:
            subs_data = {
                "touser": user_id,
                "template_id": template_id,
                "data": data,
            }
            response = requests.post(push_url, json=subs_data)
            print(response.text)


if __name__ == '__main__':
    weather()