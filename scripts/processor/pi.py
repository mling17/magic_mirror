"""
1. 获取树莓派运行信息（cpu使用量，cpu温度，内存使用量，存储使用量）
2. 控制风扇降温
3. 获取室内温湿度
4. 人体传感器
"""

import os
import time
import socket
import requests
import Adafruit_DHT
import RPi.GPIO as GPIO
from scripts.settings import TEMP_HUM_API, GPIO_DHT11, TEMP_HUM_STORAGE, GPIO_FAN, FAN_HIGH_TEMP, \
    FAN_LOW_TEMP, FAN_ENABLE_TIME
from ..storages.redis import RedisClient

sensor = Adafruit_DHT.DHT11


class Pi:
    def __init__(self):
        self.redis = RedisClient().db
        self.pi_info = {}

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

    def fan(self, pin, operate='off'):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        if operate == 'off':
            GPIO.output(pin, 0)
        else:
            GPIO.output(pin, 1)

    def run_fan(self):
        while True:
            time.sleep(0.5)
            hour = time.struct_time(time.localtime()).tm_hour
            temp = float(self.get_cpu_temperature())
            print(hour, temp)
            if temp >= FAN_HIGH_TEMP and FAN_ENABLE_TIME[0] < hour < FAN_ENABLE_TIME[1]:
                self.fan(GPIO_FAN, 'on')
            if temp <= FAN_LOW_TEMP:
                self.fan(GPIO_FAN, 'off')

    def get_pi_ip(self):
        """
                查询本机ip地址
                :return: ip
                """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    def get_cpu_use(self):
        return (str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

    def get_cpu_temperature(self):
        res = os.popen('vcgencmd measure_temp').readline()
        return res.replace("temp=", "").replace("'C\n", "")

    def get_ram_use(self):
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i == 2:
                return (line.split()[1:4])

    def get_disk_use(self):
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i == 2:
                return (line.split()[1:5])

    def pi_info_summary(self):
        # CPU informatiom
        cpu_temp = self.get_cpu_temperature()
        cpu_used = self.get_cpu_use()
        # RAM information
        # Output is in kb, here I convert it in Mb for readability
        ram_stats = self.get_ram_use()
        ram_total = round(int(ram_stats[0]) / 1000, 1)
        ram_used = round(int(ram_stats[1]) / 1000, 1)
        ram_free = round(int(ram_stats[2]) / 1000, 1)
        # disk information
        disk_stats = self.get_disk_use()
        disk_total = disk_stats[0]
        disk_used = disk_stats[1]
        disk_perc = disk_stats[3]
        self.pi_info['cpu_temp'] = cpu_temp
        self.pi_info['cpu_used'] = cpu_used
        self.pi_info['ram_state'] = {'ram_total': ram_total, 'ram_used': ram_used, 'ram_free': ram_free}
        self.pi_info['disk_state'] = {'disk_total': disk_total, 'disk_used': disk_used, 'disk_percent': disk_perc}
        self.pi_info['ip'] = self.get_pi_ip()
        return self.pi_info

    # Return information about disk space as a list (unit included)
    # Index 0: total disk space
    # Index 1: used disk space
    # Index 2: remaining disk space
    # Index 3: percentage of disk used


if __name__ == '__main__':
    pi = Pi()
    info = pi.pi_info_summary()
    print(info)
