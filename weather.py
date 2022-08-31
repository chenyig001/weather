from datetime import datetime
import requests
import json


app_id = 'wx266a7570f0f5f03f'
app_secret = '1d181e1501f1b74cc0dcebef81414128'
template_id = 'gvUhSsFN2Mh498RglcnZeAGWl84GuJsqk1T3z7yr3M8'

access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(app_id,app_secret)
res = requests.get(access_token_url).json()
access_token = res['access_token']
users = ['ozBHL59pCNzQaGm3zhapKlwVYAUc', 'ozBHL53rKBkYrelTJXdxP8ifYx5k']


def weather():
    host = 'https://jisutqybmf.market.alicloudapi.com'
    path = '/weather/query'
    appcode = 'b4c8a39e21e5415caf458b5f3217d4c6'
    # querys = 'city=%E5%BB%89%E6%B1%9F'
    city = '佛山禅城区'
    city2 = '佛山南海区'

    url = host + path + '?' + 'city={}'.format(city)
    url2 = host + path + '?' + 'city={}'.format(city2)

    header = {"Authorization": "APPCODE b4c8a39e21e5415caf458b5f3217d4c6"}
    content = requests.get(url, headers=header)  # 返回状态码
    content2 = requests.get(url2, headers=header)  # 返回状态码
    print(content)
    try:
        data = json.loads(content.text)  # 把json字符串转换为字典
        data2 = json.loads(content2.text)  # 把json字符串转换为字典
    except ValueError:
        print("try again")
    else:
        result, result2 = data.get("result"), data2.get("result")
        city, city2 = result.get("city"), result2.get("city")
        date = result.get("date")
        week = result.get("week")
        weather, weather2 = result.get("weather"), result2.get("weather")  # 天气
        temp, temp2 = result.get("temp"), result2.get("temp")        # 气温
        temphigh, temphigh2 = result.get("temphigh"), result2.get("temphigh")
        templow, templow2 = result.get("templow"), result2.get("templow")

        now = datetime.strftime(datetime.today(), "%Y-%m-%d")
        data = {
            'date': {'value': now + ' ' + week},
            'city': {'value': city},
            'weather': {'value': weather, 'color': '#f51616'},
            'temp': {'value': temp + '°C'},
            'min_teamperature': {'value': templow + '°C'},
            'max_teamperature': {'value': temphigh + '°C' + '\n'},

            'city2': {'value': city2},
            'weather2': {'value': weather2, 'color': '#f51616'},
            'temp2': {'value': temp2 + '°C'},
            'teamperature': {'value': templow + '~' + temphigh + '°C' + '\n'},
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
