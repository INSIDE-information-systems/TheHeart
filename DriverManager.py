from bme280 import *
from bme280_humidity import *
from bme280_temp import *
from bme280_pression import *
from pir import *

class DriverManager:

    liste = ("temperatureSensor","pressionSensor","humiditySensor","PIR","si1145","vl53l0")
    def driverByName(self, userChoice):
        if userChoice == self.liste[0]:
            return bme280Temperature.getValue
        elif userChoice == self.liste[1]:
            return bme280Pression.getValue
        elif userChoice == self.liste[2]:
            return bme280Humidity.getValue
        elif userChoice == self.liste[3]:
            return pir.getValue()
        else:
            raise Exception("Sensor not supported")

    def driverByIndex(self, userChoice):
        try:
            return self.driverByName(self.liste[userChoice])
        except IndexError as e:
            raise Exception("Sensor not supported")

    def isSensorSupportedName(self, sensorName):
        return sensorName in self.liste

    def isSensorSupportedIndex(self, sensorIndex):
        return (sensorIndex>0 and sensorIndex<(len(self.liste)-1))
