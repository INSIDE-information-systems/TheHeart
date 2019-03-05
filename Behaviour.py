from modes import Modes
import machine
from sensorThings import SensorThings

class Behaviour:
    def __init__(self, network, SessionData, measurement):
        print("Behaviour init")
        self.network = network
        self.sessionData = SessionData
        self.measurement = measurement
        self.sleepTime = 1000*60*self.sessionData.userConfiguration["frequency"]
        self.deepsleepPins = ["P13"]
        ignoreSensor = False

        if machine.wake_reason()[0] == machine.PIN_WAKE:
            if (machine.wake_reason()[1][0]).id() == "P13":
                ignoreSensor = True
                self.network.send("Get Configuration") # TODO: "ask configuration" message

        if not ignoreSensor:
            if self.sessionData.userConfiguration["mode"] == Modes.PERIODIC:
                self.periodic()# TODO: check frequency (par rapport aux normes)
            elif self.sessionData.userConfiguration["mode"] == Modes.RESPONSIVE:
                self.responsive()
            elif self.sessionData.userConfiguration["mode"] == Modes.PERFORMANCE:
                self.performance()# TODO: check frequency

        if self.network.hasMessage():
            print("checked message")
            try:
                self.sessionData.applyConfiguration(self.network.getMessage())
                if self.sessionData.userConfiguration["mode"] == Modes.RESPONSIVE:
                    self.deepsleepPins.append("P9")
                    self.deepsleepPins.append("P10")
            except Exception as e:
                print(e)

        machine.pin_deepsleep_wakeup(self.deepsleepPins, machine.WAKEUP_ANY_HIGH, True)

        print("Deepsleep")
        machine.deepsleep(self.sleepTime)

    def periodic(self):
        print("periodic wake")
        self.measurement.measure(self.sessionData.userConfiguration["sensorName"])
        messages = SensorThings.sensorThingify(self.measurement,self.sessionData)
        for msg in messages:
            self.network.send(msg)

    def responsive(self):
        print("responsive wake")
        self.deepsleepPins.append("P9")
        self.deepsleepPins.append("P10")
        if machine.wake_reason()[0] == machine.PIN_WAKE:
            if (machine.wake_reason()[1][0]).id() == "P9" or (machine.wake_reason()[1][0]).id() == "P10":
                self.measurement.measure(self.sessionData.userConfiguration["sensorName"])
                messages = SensorThings.sensorThingify(self.measurement,self.sessionData)
                for msg in messages:
                    self.network.send(msg)

    def performance(self):
        print("performance")
        while (not self.network.hasMessage()):
            self.measurement.measure(self.sessionData.userConfiguration["sensorName"])
            messages = SensorThings.sensorThingify(self.measurement,self.sessionData)
            for msg in messages:
                self.network.send(msg)
            utime.sleep_ms(self.sleepTime)
        self.sessionData.applyConfiguration(self.network.getMessage())
