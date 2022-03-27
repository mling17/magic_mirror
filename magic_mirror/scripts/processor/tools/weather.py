import requests
import json


class ThirdPartInfo:
    def __init__(self):
        pass

    # 获取外网IP
    def GetOuterIP(self):
        ip = requests.get('http://whatismyip.akamai.com/').text
        return ip

    # 查询IP定位
    def IPLocation(self, ip):
        url = 'http://ip-api.com/json/%s?lang=zh-CN' % ip
        while True:
            try:
                ip_dict = requests.get(url, timeout=10).json()
                print(ip_dict)
                city = ip_dict.get('city')
                status = ip_dict.get('status')
                if status == 'success':
                    return city
            except Exception as e:
                print("IPLocation Err!", str(e))
                continue

    # 输入位置，查询天气
    def weather(self, locate):
        """高德天气
        天气实况：天气，气温，风向，风力，湿度
        'lives': [{'province': '山东',
         'city': '潍坊市', 'adcode': '370700',
         'weather': '多云', 'temperature': '31', 'winddirection': '东南', 'windpower': '5', 'humidity': '64',
          'reporttime': '2021-07-17 15:31:33'}]
        :param locate:
        :return:
        """
        key = '4c5d8cfd09b55f48aee4a9f26e83aa75'
        url = 'https://restapi.amap.com/v3/weather/weatherInfo?key=%s&city=%s' % (key, locate)
        weather_dict = requests.get(url).json()
        status = weather_dict.get('status')
        # print(status, type(status))
        if status == "1":
            return weather_dict['lives'][0]
        return {}

    def forecast(self):
        url = 'https://www.weatherol.cn/api/home/getCurrAnd15dAnd24h?cityid=101120601'

        r = requests.get(url).json()

        for i in range(2, 5):
            print(r['data']['forecast15d'][i])
        return r['data']['forecast15d'][2:5]

    # 下载图片
    def downloadPic(self, url, path):
        with open(path, 'wb') as f:
            f.write(requests.get(url).content)

# if __name__ == '__main__':
#     main()
