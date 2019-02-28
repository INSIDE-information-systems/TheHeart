import Memory
import Modes

class Configuration:

    def __init__(self, jsonString):
        loadedObject = ujson.loads(Memory.restore())
        self.id = loadedObject[id]
        self.app_eui = app_eui
        self.app_key = app_key
        try:
            self.sensorDriver = loadedObject[sensorDriver]
            self.mode = loadedObject[mode]
            self.freq = loadedObject[freq]
        except Exception as e:
            self.sensorDriver = None
            self.mode = Modes.Modes.OFF
            self.freq = 60 # TODO: what should be the default frequency?

    def applyConfiguration(jsonString):
        try:
            loadedObject = ujson.loads(jsonString)
            self.sensorDriver = loadedObject[sensorDriver]
            self.mode = loadedObject[mode]
            self.freq = loadedObject[freq]
            ## TODO: check frequency
        except Exception as e:
            # TODO: send a lora message to warn the user the configuration was wrong
            # TODO: use default configuration
            pass
