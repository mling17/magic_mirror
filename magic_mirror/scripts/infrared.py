import time
import RPi.GPIO as GPIO


def sr602(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    try:
        inValue = GPIO.input(pin)
        if inValue != 0:
            print('Warning!!Someone is closing!!')
        else:
            print('Clear!')
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    for i in range(100):
        sr602(pin=4)
        time.sleep(1)
