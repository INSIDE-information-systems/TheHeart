#from bme280 import *
#from bme280_humidity import *
#from bme280_temp import *
#from bme280_pression import *
from pir import *

class DriverManager:

    def driverByName(self, userChoice):
        if userChoice == liste[0]:
            print("ChosenSensor :",userChoice)
            return bme280Temperature.getValue
        elif userChoice == liste[1]:
            print("ChosenSensor :",userChoice)
            return bme280Pression.getValue
        elif userChoice == liste[2]:
            print("ChosenSensor :",userChoice)
            return bme280Humidity.getValue
        elif userChoice == liste[3]:
            print("ChosenSensor :",userChoice)
            return pir.getValue
        else:
            raise Exception("Sensor not supported")

    def driverByIndex(self, userChoice):
        try:
            return self.driverByName(liste[userChoice])
        except IndexError as e:
            raise Exception("Sensor not supported")

    def isSensorSupportedName(self, sensorName):
        return sensorName in liste

    def isSensorSupportedIndex(self, sensorIndex):
        return (sensorIndex>0 and sensorIndex<(len(liste)-1))

#userChoice = getChosenDriver()
#userChoice = input()
liste = ("temperatureSensor","pressionSensor","humiditySensor","PIR","si1145","vl53l0")
driverManger = DriverManager()
#value = driverManger.driver(userChoice)
#print(value)
