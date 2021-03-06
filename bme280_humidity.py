from machine import Pin, I2C
from bme280 import *
from time import sleep

class HumiditySensor():
    def __init__(self):
        pass

    @property
    def getValue(self):
        i2c = I2C(0, pins=('P9','P10'))     # create and use non-default PIN assignments (P9=SDA, P10=SCL)
        init(I2C.MASTER, baudrate=115200) # init as a master
        bme = BME280(i2c=i2c)
        return bme.getHumidite()

# bme280Humidity = HumiditySensor()
# bme280Humidity.getValue
