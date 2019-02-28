from modes import Modes
import machine
import SensorThings

class Behaviour:
    def __init__(self, network, config):
        self.network = network
        self.configuration = config
        self.sleepTime = 1000*60*self.configuration.frequency # TODO: find a more elegant way to set the time

        if self.mode = Modes.PERIODIC:
            self.periodic()# TODO: get periodicity
        elif self.mode = Modes.RESPONSIVE:
            self.responsive()
        elif self.mode = Modes.PERFORMANCE:
            self.performance()# TODO: set check frequency

        if self.network.hasMessage():
            # TODO: handle reconf
            self.configuration()

        machine.deepsleep(self.sleepTime)

    def periodic():
        value = sensor.getValue()
        # TODO: SensorThings
        network.send(value)

    def responsive():
        machine.pin_deepsleep_wakeup(["P13"], machine.WAKEUP_ANY_HIGH, False)# TODO: set the right pin
        if machine.wake_reason()[0] == machine.PIN_WAKE:
            #if machine.wake_reason()[1] == the pin of the pir sensor
            value = sensor.getValue()
            network.send(value)
        # TODO: what should be done if the wakeup is triggered by the button?

    def performance():
        while (not self.network.hasMessage()):
            value = sensor.getValue()
            network.send(value)
            utime.sleep_ms(self.sleepTime)
        # TODO: handle reconf
        self.configuration()
