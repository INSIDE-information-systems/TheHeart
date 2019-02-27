from machine import Pin, I2C
from bme280 import *
from time import sleep

class TemperatureSensor():

    @property
    def getValue(self):
        return bme.getTemperature

i2c = I2C(scl=Pin(22), sda=Pin(23))
bme = BME280(i2c=i2c)

bme280Temperature = TemperatureSensor()
bme280Temperature.getValue
