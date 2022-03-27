import os
#import Rpi.GPIO as GPIO


class Screen:
    """
    屏幕控制类，人体传感器感应人体是否接近，接近打开屏幕，led开启，离开一段延时后关闭屏幕及led
    """
    def __init__(self):
        self.photo_sensor = 19  # 光电传感器所连GPIO脚（空闲时高电平）
        self.LED_Pin = 26

    # 检查是否有人靠近(GPIO0)
    def isSomeoneClose(self):
        input = GPIO.input(self.photo_sensor)
        if input == 1:  # 人已离开
            return 1
        else:  # 有人靠近
            return 0

    def setLEDon(self):
        GPIO.output(self.LED_Pin, GPIO.HIGH)  # 输出高电平

    def setLEDoff(self):
        GPIO.output(self.LED_Pin, GPIO.LOW)  # 输出低电平

    # 唤醒屏幕
    def screenWakeUp(self):
        os.popen('sudo xset dpms force on')  # 唤醒

    # 检查屏幕的点亮状态
    def checkScreenStatOn(self):
        try:
            stat = os.popen('sudo xset q').readlines()[-1].strip()
        except:
            return True
        print(stat)
        if 'Monitor is Off' in stat:
            return False
        elif 'Monitor is On' in stat:
            return True

    # 关闭屏幕
    def setScreenOff(self):
        os.popen('sudo xset dpms force off')  # 立即关闭屏幕
    
obj = Screen()
obj.setScreenOff()
import time
time.sleep(5)
obj.screenWakeUp()

