import FlashMemory
import DriverManager
import Modes

class SessionData:

    def __init__(self, jsonString):
        try:
            self.staticConfiguration = ujson.loads(FlashMemory.restore("static"))
        except Exception as e:
            raise # TODO: what should we do if the Heart is not configured at all?

        try:
            self.userConfiguration = ujson.loads(FlashMemory.restore("user"))
        except Exception as e:
            #default configuration
            self.userConfiguration = {
                "mode" : Modes.OFF,
                "sensorName" : None,
                "frequency" : 60 # TODO: should the default frequency be 1 hour?
            }

        try:
            self.lastGpsCoordinates = ujson.loads(FlashMemory.restore("gps"))
        except Exception as e:
            self.lastGpsCoordinates = None# TODO: put 0,0 or something

    def applyConfiguration(jsonString):
        sensorMode = [Modes.OFF, Modes.RESPONSIVE, Modes.PERIODIC]
        newConfiguration = ujson.loads(jsonString)
        try:
            self.userConfiguration["mode"] = sensorMode[newConfiguration["sensorMode"]]
        except KeyError as e:
            pass
        try:
            if DriverManager.isSensorSupportedIndex(sensorMode[newConfiguration["sensorType"]]):
                self.userConfiguration["sensorName"] = DriverManager.driverByIndex(sensorMode[newConfiguration["sensorType"]])
        except KeyError as e:
            pass
        try:
            self.userConfiguration["frequency"] = sensorMode[newConfiguration["sensorParameter"]["collectPeriod"]]
        except KeyError as e:
            pass
        # TODO: parse from sensorthing format

    def saveGPS(gps):
        FlashMemory.save("gps",ujson.dumps(gps))
        # TODO: check if gps is serializable
