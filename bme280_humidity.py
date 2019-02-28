from machine import Pin, I2C
from bme280 import *
from time import sleep

class HumiditySensor():

    @property
    def getValue(self):
        return bme.getHumidite

i2c = I2C(scl=Pin(22), sda=Pin(23))
bme = BME280(i2c=i2c)

bme280Humidity = HumiditySensor()
bme280Humidity.getValue
