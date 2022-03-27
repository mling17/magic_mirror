"""
1. 获取树莓派运行信息（cpu使用量，cpu温度，内存使用量，存储使用量）
2. 控制风扇降温
3. 获取室内温湿度
4. 人体传感器
"""
import time
import requests
import Adafruit_DHT
from magic_mirror.scripts.settings import TEMP_HUM_API, GPIO_DHT11, TEMP_HUM_STORAGE
from ..storages.rediss import RedisClient

sensor = Adafruit_DHT.DHT11


class Pi:
    def __init__(self):
        self.redis = RedisClient().db

    def dht11(self):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO_DHT11)
        result = False
        if humidity is not None and temperature is not None:
            print(time.ctime(), 'Temp={0:0.1f}*C,Humidity={1:0.1f}%'.format(temperature, humidity))
            self.redis.hset('house_temp_hum', mapping={'temp': temperature, 'hum': humidity})
            if TEMP_HUM_STORAGE:
                result = requests.post(url=TEMP_HUM_API, data={"temperature": temperature, "humidity": humidity}).text
            if result == 'ok':
                result = True
        return result
