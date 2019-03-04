import FlashMemory
import DriverManager
import Modes
import ujson

class SessionData:

    def __init__(self):
        try:
            self.staticConfiguration = ujson.loads(FlashMemory.FlashMemory.restore("static"))
        except Exception as e:
            raise # TODO: what should we do if the Heart is not configured at all?

        try:
            self.userConfiguration = ujson.loads(FlashMemory.FlashMemory.restore("user"))
        except Exception as e:
            #default configuration
            self.userConfiguration = {
                "mode" : Modes.Modes.OFF,
                "sensorName" : None,
                "frequency" : 60 # TODO: should the default frequency be 1 hour?
            }

        try:
            self.lastGpsCoordinates = ujson.loads(FlashMemory.FlashMemory.restore("gps"))
        except Exception as e:
            self.lastGpsCoordinates = None# TODO: put 0,0 or something

    def applyConfiguration(jsonString):
        sensorMode = [Modes.Modes.OFF, Modes.Modes.RESPONSIVE, Modes.Modes.PERIODIC]
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
        FlashMemory.FlashMemory.save("gps",ujson.dumps(gps))
        # TODO: check if gps is serializable
