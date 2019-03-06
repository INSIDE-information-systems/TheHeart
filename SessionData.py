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
            machine.deepsleep()


        try:
            self.userConfiguration = ujson.loads(FlashMemory.FlashMemory.restore("user"))
        except Exception as e:
            #default configuration
            print(e)
            self.userConfiguration = {
                "mode" : Modes.Modes.OFF,
                "sensorName" : None,
                "frequency" : 360
            }

        try:
            self.lastGpsCoordinates = ujson.loads(FlashMemory.FlashMemory.restore("gps"))
        except Exception as e:
            print("GPS file:")
            print(e)
            self.lastGpsCoordinates = None

    def applyConfiguration(self, jsonString):
        # TODO: send error if a parameter is wrong
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
        print("applied configuration:")
        print("  mode:")
        print(self.userConfiguration["mode"])
        print("  sensor:")
        print(self.userConfiguration["sensorName"])
        print("  frequency:")
        print(self.userConfiguration["frequency"])

    def saveGPS(gps):
        try:
            FlashMemory.FlashMemory.save("gps",ujson.dumps(gps))
        except Exception as e:
            print("Error saving GPS")
            print(e)
