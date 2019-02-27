from machine import Pin, I2C
from bme280 import *
from time import sleep

class PressionSensor():

    @property
    def getValue(self):
        return bme.getPression

i2c = I2C(scl=Pin(22), sda=Pin(23))
bme = BME280(i2c=i2c)

bme280Pression = PressionSensor()
bme280Pression.getValue
