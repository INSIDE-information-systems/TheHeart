from modes import Modes
import machine

class Behaviour:
    def __init__(self, network, confign mode = Modes.OFF):
        self.network = network
        self.configuration = config
        if self.network.hasMessage():
            # TODO: handle reconf
            self.configuration()
        else:
            if self.mode = Modes.OFF
                minutes = 1 # TODO: find a more elegant way to set the time
                self.off(1000*60*minutes)# TODO: set check frequency
            elif self.mode = Modes.PERIODIC:
                self.periodic(config.)# TODO: get periodicity
            elif self.mode = Modes.RESPONSIVE:
                self.responsive()
            elif self.mode = Modes.PERFORMANCE:
                self.performance()# TODO: set check frequency
            elif self.mode = Modes.UNAUTHORISED:
                self.off()# TODO: set check frequency

    def off(sleepTime):
        machine.deepsleep(sleepTime)

    def periodic(sleepTime):
        value = sensor.getValue()
        network.send(value)
        machine.deepsleep(sleepTime)

    def responsive():
        machine.pin_deepsleep_wakeup(["P13"], machine.WAKEUP_ANY_HIGH, False)# TODO: set the right pin
        value = sensor.getValue()
        network.send(value)
        machine.deepsleep(sleepTime)

    def performance(sleepTime):
        while (not self.network.hasMessage()):
            value = sensor.getValue()
            network.send(value)
            utime.sleep_ms(sleepTime)
        # TODO: handle reconf
        self.configuration()
