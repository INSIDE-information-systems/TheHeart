from machine import Pin, I2C
from bme280 import *
from time import sleep

class PressionSensor():
    def __init__(self,i2c,bme):

        self.i2c = I2C(0, pins=('P9','P10'))     # create and use non-default PIN assignments (P9=SDA, P10=SCL)
        i2c.init(I2C.MASTER, baudrate=115200) # init as a master
        self.bme = BME280(i2c=i2c)

    @property
    def getValue(self):
        i2c = I2C(0, pins=('P9','P10'))     # create and use non-default PIN assignments (P9=SDA, P10=SCL)
        i2c.init(I2C.MASTER, baudrate=115200) # init as a master

        #i2c = I2C(scl=Pin(22), sda=Pin(23))
        bme = BME280(i2c=i2c)
        return bme.getPression

# i2c = I2C(0, pins=('P9','P10'))     # create and use non-default PIN assignments (P9=SDA, P10=SCL)
# i2c.init(I2C.MASTER, baudrate=115200) # init as a master
# #i2c = I2C(scl=Pin(22), sda=Pin(23))
# bme = BME280(i2c=i2c)
#
# bme280Pression = PressionSensor()
# bme280Pression.getValue
