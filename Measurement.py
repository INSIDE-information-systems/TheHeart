import DriverManager

class Measurement:
    def __init__(self, gps):
        self.gpsInstance = gps
        self.value = None
        self.location = None
        self.date = None
    def measure(self, sensorName):
        try:
            self.value = DriverManager.driver(sensorName)
        except Exception as e:
            pass
            # TODO: how to report a Measurement error?
        self.date = self.gpsInstance.getTime()
        self.location = self.gpsInstance.getLocation()
