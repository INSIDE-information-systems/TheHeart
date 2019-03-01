import FlashMemory
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
            self.lastGpsCoordinates = # TODO: put 0,0 or something


    def applyConfiguration(jsonString):
        # TODO: parse from sensorthing format
