"""
1. 获取树莓派运行信息（cpu使用量，cpu温度，内存使用量，存储使用量）
2. 控制风扇降温
3. 获取室内温湿度
4. 人体传感器
"""

import os
import time
import json
import socket
import requests
import multiprocessing
import Adafruit_DHT
import RPi.GPIO as GPIO
from loguru import logger
from settings import TEMP_HUM_API, GPIO_DHT11, TEMP_HUM_STORAGE, GPIO_FAN, FAN_HIGH_TEMP, FAN_LOW_TEMP, \
    FAN_ENABLE_TIME, ENABLE_FAN, ENABLE_PI_INFO, ENABLE_DHT11, CYCLE_FAN, CYCLE_INFO, CYCLE_DHT11
from .redis_conn import RedisClient

sensor = Adafruit_DHT.DHT11

fan_process, info_process, dht11_process = None, None, None


class Pi:
    def __init__(self):
        self.redis = RedisClient().db
        self.pi_info = {}

    def dht11(self):
        return Adafruit_DHT.read_retry(sensor, GPIO_DHT11)
        # humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO_DHT11)
        # result = False
        # if humidity is not None and temperature is not None:
        #     print(time.ctime(), 'Temp={0:0.1f}*C,Humidity={1:0.1f}%'.format(temperature, humidity))
        #     self.redis.hset('house_temp_hum', mapping={'temp': temperature, 'hum': humidity})
        #     if TEMP_HUM_STORAGE:
        #         result = requests.post(url=TEMP_HUM_API, data={"temperature": temperature, "humidity": humidity}).text
        #     if result == 'ok':
        #         result = True
        # return result

    def fan(self, pin, operate='off'):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        if operate == 'off':
            GPIO.output(pin, 0)
        else:
            GPIO.output(pin, 1)

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


class PiRun(object):
    def __init__(self):
        self.pi = Pi()

    def run_fan(self):
        """
        每一段时间获取一次cpu温度，超过阈值则运行风扇，低于阈值停止风扇
        """
        if not ENABLE_FAN:
            logger.info('Fan not enabled, exit')
            return
        while True:
            hour = time.struct_time(time.localtime()).tm_hour
            temp = float(self.pi.get_cpu_temperature())
            if temp >= FAN_HIGH_TEMP and FAN_ENABLE_TIME[0] < hour < FAN_ENABLE_TIME[1]:
                self.pi.fan(GPIO_FAN, 'on')
            if temp <= FAN_LOW_TEMP:
                self.pi.fan(GPIO_FAN, 'off')
            time.sleep(CYCLE_FAN)

    def run_pi_info(self):
        """
        每隔一段时间获取一次pi的信息，并写入到redis
        """
        if not ENABLE_PI_INFO:
            logger.info('Pi info not enabled, exit')
            return
        while True:
            pi_info = self.pi.pi_info_summary()
            ram_state = pi_info.get('ram_state')
            disk_state = pi_info.get('disk_state')
            pi_info['ram_state'] = json.dumps(ram_state)
            pi_info['disk_state'] = json.dumps(disk_state)
            self.pi.redis.hmset('pi_info', pi_info)  # 存入redis
            time.sleep(CYCLE_INFO)

    def run_dht11(self):
        """
        每隔一段时间获取一次室内温湿度
        """
        if not ENABLE_DHT11:
            logger.info('DHT11 not enabled, exit')
            return
        while True:
            logger.info('Get indoor humidity and temperature.')
            humidity, temperature = self.pi.dht11()
            sleep = CYCLE_DHT11
            if humidity is not None and temperature is not None:
                logger.info('Temp={0:0.1f}*C,Humidity={1:0.1f}%'.format(temperature, humidity))
                self.pi.redis.hset('house_temp_hum', mapping={'temp': temperature, 'hum': humidity})  # 存入redis
                if TEMP_HUM_STORAGE:
                    try:
                        result = requests.post(url=TEMP_HUM_API,
                                               data={"temperature": temperature, "humidity": humidity}, timeout=1).text
                        logger.info(f'Temperature and humidity storage success.')
                        if result != 'ok':
                            sleep = 1
                    except Exception as e:
                        sleep = 1
            else:
                print(f'err-->,hum:{humidity},temp:{temperature}')
                sleep = 1
            time.sleep(sleep)

    def run(self):
        global fan_process, info_process, dht11_process
        try:
            logger.info('starting pi process...')
            if ENABLE_FAN:
                fan_process = multiprocessing.Process(
                    target=self.run_fan)
                logger.info(f'starting fan control, pid {fan_process.pid}...')
                fan_process.start()

            if ENABLE_PI_INFO:
                info_process = multiprocessing.Process(
                    target=self.run_pi_info)
                logger.info(f'starting get pi information, pid {info_process.pid}...')
                info_process.start()

            if ENABLE_DHT11:
                dht11_process = multiprocessing.Process(
                    target=self.run_dht11)
                logger.info(f'starting get indoor temperature and humidity, pid {dht11_process.pid}...')
                dht11_process.start()

            fan_process and fan_process.join()
            info_process and info_process.join()
            dht11_process and dht11_process.join()
        except KeyboardInterrupt:
            logger.info('received keyboard interrupt signal')
            fan_process and fan_process.terminate()
            info_process and info_process.terminate()
            dht11_process and dht11_process.terminate()
        finally:
            # must call join method before calling is_alive
            fan_process and fan_process.join()
            info_process and info_process.join()
            dht11_process and dht11_process.join()
            logger.info(
                f'Fan control is {"alive" if fan_process.is_alive() else "dead"}')
            logger.info(
                f'Get pi information is {"alive" if info_process.is_alive() else "dead"}')
            logger.info(
                f'Get indoor temperature and humidity is {"alive" if dht11_process.is_alive() else "dead"}')
            logger.info('Pi terminated')


if __name__ == '__main__':
    pi = Pi()
    info = pi.dht11()
    print(info)
