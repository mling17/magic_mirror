import Adafruit_DHT
import requests
import time


sensor = Adafruit_DHT.DHT11
gpio = 17
url = "http://127.0.0.1:8000/temp_hum/"
def get_data():
    flag = True
    humidity,temperature = Adafruit_DHT.read_retry(sensor,gpio)
    if humidity is not None and temperature is not None:
        print(time.ctime(),'Temp={0:0.1f}*C,Humidity={1:0.1f}%'.format(temperature,humidity))
        res=requests.post(url=url,data={"temperature":temperature,"humidity":humidity}).text
        if res != 'ok':
            get_data()
    else:
        get_data()
if __name__ == '__main__':
    try:
        get_data()
    except Exception as e:
        print(e)
