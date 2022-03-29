import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 17
h,t = Adafruit_DHT.read_retry(sensor,pin)
if h is not None and t is not None:
    print(h,t)
else:
    print('failed')