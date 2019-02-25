class Configuration:
    def __init__(self, id, sensorDriver, mode, freq, app_eui, app_key):
        self.id = id # TODO: find a more elegant way to do that
        self.sensorDriver = sensorDriver
        self.mode = mode
        self.freq = freq #time in minutes
        self.app_eui = app_eui
        self.app_key = app_key
    def applyConfiguration(jsonString):
        loadedObject = ujson.loads(jsonString)
        self.id = loadedObject[id]
        self.sensorDriver = loadedObject[sensorDriver]
        self.mode = loadedObject[mode]
        self.freq = loadedObject[freq]
        # TODO: instanciate sensor object
