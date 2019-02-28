
from machine import UART,RTC
import utime as time
from time import sleep
import adafruit_gps
from adafruit_gps import *

class UltimateGPS:
    def __init__(self):
        uart = UART(2, baudrate=9600)
        uart.init(9600, bits=8, parity=None, stop=1, tx=17,rx=16)

        gps = adafruit_gps.GPS(uart)
        gps.send_command('PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        gps.send_command('PMTK220,1000')
        gps.update()
    def isFixed(self):
        if not gps.has_fix:
            gps.update()
        return True

    def getLocation(self):
        return (gps.latitude,gps.longitude)
    def getLatitude(self):
        return gps.latitude
    def getLongitude(self):
        return gps.longitude
    def getTime(self):
        day = str(gps.timestamp_utc[2])
        month = str(gps.timestamp_utc[1])
        year = str(gps.timestamp_utc[0])
        hour = str(gps.timestamp_utc[3]+1)
        minute = str(gps.timestamp_utc[4])
        sec = str(gps.timestamp_utc[5])
        date = day+"/"+month+"/"+year+" "+hour+":"+minute+":"+sec
        return date

uart = UART(2, baudrate=9600)
uart.init(9600, bits=8, parity=None, stop=1, tx=17,rx=16)

gps = adafruit_gps.GPS(uart)
ultimate = UltimateGPS()
# while not gps.has_fix:
#     gps.update()
print("has_fix: ",ultimate.isFixed())
print("date: ",ultimate.getTime())
print("Lat: ",ultimate.getLatitude())
print("Long: ",ultimate.getLongitude())
print("location: ",ultimate.getLocation())
