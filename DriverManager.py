from bme280 import *
from bme280_humidity import *
from bme280_temp import *
from bme280_pression import *

class DriverManager:

    def driver(self, userChoice):
        if userChoice == liste[0]:
            print("ChosenSensor :",userChoice)
            return bme280Temperature.getValue
        elif userChoice == liste[1]:
            print("ChosenSensor :",userChoice)
            return bme280Pression.getValue
        elif userChoice == liste[2]:
            print("ChosenSensor :",userChoice)
            return bme280Humidity.getValue
        else:
            print("please, choose your sensor")
            userChoice = input()

#userChoice = getChosenDriver()
userChoice = input()
liste = ("temperatureSensor","pressionSensor","humiditySensor","si1145","vl53l0")
driverManger = DriverManager()
value = driverManger.driver(userChoice)
print(value)
