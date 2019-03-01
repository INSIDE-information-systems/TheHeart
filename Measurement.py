import DriverManager

class Measurement:
    def __init__(self, gps):
        self.gpsInstance = gps
        self.value = None
        self.location = None
        self.date = None
    def measure(sensorName):
        self.value = DriverManager.driver(sensorName)
        self.date = gps.getTime()
        self.location = gps.getLocation()
