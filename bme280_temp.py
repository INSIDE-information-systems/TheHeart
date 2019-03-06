from machine import Pin, I2C
from bme280 import *
from time import sleep

class TemperatureSensor():
    def __init__(self):
        pass

    @property
    def getValue(self):
        self.i2c = I2C(0, pins=('P9','P10'))     # create and use non-default PIN assignments (P9=SDA, P10=SCL)
        self.i2c.init(I2C.MASTER, baudrate=115200) # init as a master
        self.bme = BME280(i2c=self.i2c)
        return self.bme.getTemperature()