from modes import Modes
import machine
import SensorThings

class Behaviour:
    def __init__(self, network, SessionData, measurement):
        self.network = network
        self.sessionData = SessionData
        self.measurement = measurement
        self.sleepTime = 1000*60*self.sessionData.frequency # TODO: find a more elegant way to set the time

        if self.mode == Modes.PERIODIC:
            self.periodic()# TODO: check frequency
        elif self.mode == Modes.RESPONSIVE:
            self.responsive()
        elif self.mode == Modes.PERFORMANCE:
            self.performance()# TODO: check frequency

        if self.network.hasMessage():
            self.sessionData.applyConfiguration(self.network.getMessage())

        machine.deepsleep(self.sleepTime)

    def periodic():
        self.measurement.measure(self.sessionData.sensorName)
        msg = SensorThings.sensorthingify(self.measure)
        network.send(msg)

    def responsive():
        machine.pin_deepsleep_wakeup(["P13"], machine.WAKEUP_ANY_HIGH, False)# TODO: set the right pin
        # TODO: what should be done if the wakeup is triggered by the button?
        #if machine.wake_reason()[1] == the pin of the pir sensor
        if machine.wake_reason()[0] == machine.PIN_WAKE:
            self.measurement.measure(self.sessionData.sensorName) # TODO: pir sensor driver
            msg = SensorThings.sensorthingify(self.measure)
            network.send(msg)

    def performance():
        while (not self.network.hasMessage()):
            self.measurement.measure(self.sessionData.sensorName) # TODO: pir sensor driver
            msg = SensorThings.sensorthingify(self.measure)
            network.send(msg)
            utime.sleep_ms(self.sleepTime)
        self.sessionData.applyConfiguration(self.network.getMessage())
