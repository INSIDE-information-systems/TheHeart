from modes import Modes
import machine

class Behaviour:
    def __init__(self, network, config):
        self.network = network
        self.configuration = config
        self.sleepTime = 1000*60*self.configuration.frequency # TODO: find a more elegant way to set the time
        if self.network.hasMessage():
            # TODO: handle reconf
            self.configuration()
        else:
            if self.mode = Modes.OFF
                self.off()# TODO: set check frequency
            elif self.mode = Modes.PERIODIC:
                self.periodic()# TODO: get periodicity
            elif self.mode = Modes.RESPONSIVE:
                self.responsive()
            elif self.mode = Modes.PERFORMANCE:
                self.performance()# TODO: set check frequency
            elif self.mode = Modes.UNAUTHORISED:
                self.off()# TODO: set check frequency

    def off(sleepTime):
        machine.deepsleep(self.sleepTime)

    def periodic(sleepTime):
        value = sensor.getValue()
        network.send(value)
        machine.deepsleep(self.sleepTime)

    def responsive():
        machine.pin_deepsleep_wakeup(["P13"], machine.WAKEUP_ANY_HIGH, False)# TODO: set the right pin
        value = sensor.getValue()
        network.send(value)
        machine.deepsleep(self.sleepTime)

    def performance(sleepTime):
        while (not self.network.hasMessage()):
            value = sensor.getValue()
            network.send(value)
            utime.sleep_ms(self.sleepTime)
        # TODO: handle reconf
        self.configuration()
