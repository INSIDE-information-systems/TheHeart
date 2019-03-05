from machine import UART,RTC
import utime as time
from time import sleep
import adafruit_gps
from adafruit_gps import *
import utime

class UltimateGPS:
    def __init__(self):
        self.startTime = utime.ticks_ms()
        # this uses the UART_1 default pins for TXD and RXD (``P3`` and ``P4``)
        uart = UART(1, baudrate=9600)
        gps = adafruit_gps.GPS(uart)
        gps.send_command('PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        gps.send_command('PMTK220,1000')
        gps.update()
    def isFixed(self):
        if (utime.ticks_ms()-self.startTime)/1000<600: #GPS fix timeout = 10 mins
            if not gps.has_fix:
                gps.update()
                return False
            return True
        else:
            raise Exception("GPS timeout") # TODO: custom exception

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
    def calculDistance(lat1,lat2,lon1,lon2):
        dlon = lon1 - lon2
        dlat = lat1 - lat2
        if dlat>0.00001 and dlon>0.00001:
            print("update")
            return True
        return False
# this uses the UART_1 default pins for TXD and RXD (``P3`` and ``P4``)
uart = UART(1, baudrate=9600)

gps = adafruit_gps.GPS(uart)
ultimate = UltimateGPS()
# while not gps.has_fix:
#     gps.update()
print("has_fix: ",ultimate.isFixed())
print("date: ",ultimate.getTime)
print("Lat: ",ultimate.getLatitude())
print("Long: ",ultimate.getLongitude())
print("location: ",ultimate.getLocation())
