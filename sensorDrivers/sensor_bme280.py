from machine import Pin, I2C
from bme280 import *
from time import sleep

class bme280Sensor():

    def __init__(self,i2c,sensor):
        self.i2c = I2C(scl=Pin(22), sda=Pin(23))
        self.sensor = BME280(i2c=i2c)

    @property
    def getValues(self):
        while True:
            print(bme.getTemperature)
            print(bme.getHumidite)
            print(bme.getPression)
            print('-' * 40)
            sleep(1)

i2c = I2C(scl=Pin(22), sda=Pin(23))
bme = BME280(i2c=i2c)
bme280 = bme280Sensor(i2c, bme)
bme280.getValues()
print('-' * 40)
