from machine import Pin, I2C
from bme280 import *
from time import sleep

class TemperatureSensor():

    # def __init__(self,i2c,sensor):
    #     self.i2c = I2C(scl=Pin(22), sda=Pin(23))
    #     self.sensor = BME280(i2c=i2c)
    @property
    def getValue(self):
        return bme.getTemperature()

i2c = I2C(scl=Pin(22), sda=Pin(23))
bme = BME280(i2c=i2c)

bme280 = TemperatureSensor()
bme280.getValue()
