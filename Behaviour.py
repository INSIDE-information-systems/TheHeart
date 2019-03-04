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

        if self.sessionData.userConfiguration["mode"] == Modes.PERIODIC:
            self.periodic()# TODO: check frequency
        elif self.sessionData.userConfiguration["mode"] == Modes.RESPONSIVE:
            self.responsive()
        elif self.sessionData.userConfiguration["mode"] == Modes.PERFORMANCE:
            self.performance()# TODO: check frequency

        if self.network.hasMessage():
            print("checked message")
            try:
                self.sessionData.applyConfiguration(self.network.getMessage())
            except Exception as e:
                print(e)

        print("Deepsleep")
        machine.deepsleep(self.sleepTime)

    def periodic(self):
        print("periodic wake")
        self.measurement.measure(self.sessionData.userConfiguration["sensorName"])
        msg = SensorThings.sensorThingify(self.measurement,self.sessionData)
        self.network.send(msg)

    def responsive(self):
        print("responsive wake")
        machine.pin_deepsleep_wakeup(["P13"], machine.WAKEUP_ANY_HIGH, False)# TODO: set the right pin
        # TODO: what should be done if the wakeup is triggered by the button?
        #if machine.wake_reason()[1] == the pin of the pir sensor
        if machine.wake_reason()[0] == machine.PIN_WAKE:
            self.measurement.measure(self.sessionData.userConfiguration["sensorName"]) # TODO: pir sensor driver
            msg = SensorThings.sensorThingify(self.measurement,self.sessionData)
            self.network.send(msg)

    def performance(self):
        print("performance")
        while (not self.network.hasMessage()):
            self.measurement.measure(self.sessionData.userConfiguration["sensorName"]) # TODO: pir sensor driver
            msg = SensorThings.sensorThingify(self.measurement,self.sessionData)
            self.network.send(msg)
            utime.sleep_ms(self.sleepTime)
        self.sessionData.applyConfiguration(self.network.getMessage())
