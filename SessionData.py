import FlashMemory
import DriverManager
import Modes
import ujson

class SessionData:

    def __init__(self):
        try:
            self.staticConfiguration = ujson.loads(FlashMemory.FlashMemory.restore("static"))
        except Exception as e:
            print("static configuration:")
            print(e)

            # TODO: what should we do if the Heart is not configured at all :
            machine.deepsleep(self.sleepTime)



        try:
            self.userConfiguration = ujson.loads(FlashMemory.FlashMemory.restore("user"))
        except Exception as e:
            #default configuration
            print(e)
            self.userConfiguration = {
                "mode" : Modes.Modes.OFF,
                "sensorName" : None,
                "frequency" : 60 # TODO: should the default frequency be 1 hour?
            }

        try:
            self.lastGpsCoordinates = ujson.loads(FlashMemory.FlashMemory.restore("gps"))
        except Exception as e:
            print("GPS file:")
            print(e)
            self.lastGpsCoordinates = None# TODO: put 0,0 or something

    def applyConfiguration(self, jsonString):
        sensorMode = [Modes.Modes.OFF, Modes.Modes.RESPONSIVE, Modes.Modes.PERIODIC]
        try:
            newConfiguration = ujson.loads(jsonString)
            self.userConfiguration["mode"] = sensorMode[newConfiguration["sensorMode"]]
        except KeyError as e:
            pass
        try:
            newConfiguration = ujson.loads(jsonString)
            if DriverManager.isSensorSupportedIndex(sensorMode[newConfiguration["sensorType"]]):
                self.userConfiguration["sensorName"] = DriverManager.driverByIndex(sensorMode[newConfiguration["sensorType"]])
        except KeyError as e:
            pass
        try:
            newConfiguration = ujson.loads(jsonString)
            self.userConfiguration["frequency"] = sensorMode[newConfiguration["sensorParameter"]["collectPeriod"]]
        except KeyError as e:
            pass
        # TODO: parse from sensorthing format

    def saveGPS(gps):
        FlashMemory.FlashMemory.save("gps",ujson.dumps(gps))
        # TODO: check if gps is serializable
