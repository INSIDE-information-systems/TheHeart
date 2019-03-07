from bmp180 import *
from machine import I2C, Pin




class BMP180TEMP():
    i2c = I2C(0, pins=('P9','P10'))     # create and use non-default PIN assignments (P9=SDA, P10=SCL)
    bmp180 = BMP180( i2c )

    def getValue():
        i2c = I2C(0, pins=('P9','P10'))     # create and use non-default PIN assignments (P9=SDA, P10=SCL)
        bmp180 = BMP180( i2c )
        temp = bmp180.temperature
        print( "Temperature: %.2f" % temp )



#bmp180 = BMP180TEMP();
# print(bmp180.getValue())
