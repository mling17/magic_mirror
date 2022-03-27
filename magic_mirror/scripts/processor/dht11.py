import Adafruit_DHT
import requests
import time
from magic_mirror.scripts.settings import GPIO_DHT11, TEMP_HUM_API

sensor = Adafruit_DHT.DHT11


def get_data():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO_DHT11)
    if humidity is not None and temperature is not None:
        print(time.ctime(), 'Temp={0:0.1f}*C,Humidity={1:0.1f}%'.format(temperature, humidity))
        res = requests.post(url=TEMP_HUM_API, data={"temperature": temperature, "humidity": humidity}).text
        if res != 'ok':
            get_data()
    else:
        get_data()


if __name__ == '__main__':
    try:
        get_data()
    except Exception as e:
        print(e)
