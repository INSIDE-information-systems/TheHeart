from DriverManager import DriverManager
import time

class Measurement:
    def __init__(self, gps, driverManager):
        self.driverManager = driverManager
        self.gpsInstance = gps
        self.value = None
        self.location = None
        self.date = None
    def measure(self, sensorName):
        try:
            self.value = self.driverManager.driverByName(sensorName)
            print("measurement done")
            print(self.value)
        except Exception as e:
            print(e)
            pass
            # TODO: how to report a Measurement error?
        try:
            while not self.gpsInstance.isFixed():
                print("GPS not fixed yet")
                time.sleep(2)
                pass
            self.date = self.gpsInstance.getTime()
            self.location = self.gpsInstance.getLocation()
            print("measurement located")
        except Exception as e:
            print(e)
            # TODO: handle gps timeout : custom ex
            pass
