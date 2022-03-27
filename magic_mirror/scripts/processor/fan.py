import time, os
import RPi.GPIO as GPIO


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    res = res.split('=')[-1].split("'")[0]
    return float(res)


def fan(pin, operate='off'):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    if operate == 'off':
        GPIO.output(pin, 0)
    else:
        GPIO.output(pin, 1)


def main():
    while True:
        time.sleep(0.5)
        hour = time.struct_time(time.localtime()).tm_hour
        temp = getCPUtemperature()
        print(hour, temp)
        if temp >= 65 and 6 < hour < 23:
            fan(26, 'on')
        if temp <= 55:
            fan(26, 'off')


if __name__ == '__main__':
    main()
