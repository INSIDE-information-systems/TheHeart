from DriverManager import DriverManager

class Measurement:
    def __init__(self, gps, driverManager):
        self.driverManger = driverManager
        self.gpsInstance = gps
        self.value = None
        self.location = None
        self.date = None
    def measure(self, sensorName):
        print("measure:" + sensorName)
        try:
            self.value = self.driverManager.driverByName(sensorName)
            print("measurement done")
            print(str(self.value))
        except Exception as e:
            print(e)
            pass
            # TODO: how to report a Measurement error?
        try:
            while not self.gpsInstance.isFixed():
                pass
            self.date = self.gpsInstance.getTime()
            self.location = self.gpsInstance.getLocation()
            print("measurement located")
        except Exception as e:
            print(e)
            # TODO: handle gps timeout
            pass
