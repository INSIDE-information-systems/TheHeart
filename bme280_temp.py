from machine import Pin, I2C
from bme280 import *
from time import sleep

class TemperatureSensor():
    def __init__(self):

        i2c = I2C(0, pins=('P9','P10'))     # create and use non-default PIN assignments (P9=SDA, P10=SCL)
        init(I2C.MASTER, baudrate=115200) # init as a master
        bme = BME280(i2c=i2c)

    @property
    def getValue(self):
        i2c = I2C(0, pins=('P9','P10'))     # create and use non-default PIN assignments (P9=SDA, P10=SCL)
        init(I2C.MASTER, baudrate=115200) # init as a master

        #i2c = I2C(scl=Pin(22), sda=Pin(23))
        bme = BME280(i2c=i2c)
        return bme.getTemperature

bme280Temperature = TemperatureSensor()
# bme280Temperature.getValue
