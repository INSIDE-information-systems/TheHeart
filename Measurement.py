import DriverManager

class Measurement:
    def __init__(self, gps):
        self.gpsInstance = gps
        self.value = None
        self.location = None
        self.date = None
    def measure(sensorName):
        try:
            self.value = DriverManager.driver(sensorName)
        except Exception as e:
            # TODO: how to report a Measurement error?
        self.date = gps.getTime()
        self.location = gps.getLocation()
