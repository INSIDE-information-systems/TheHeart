from network import LoRa
import socket
import ubinascii
import time

class Network:
    """
    Manages communication with a LoRaWAN network.
    Requires keys appeui and appkey in the dictionary config.staticConfiguration.
    """
    def __init__(self, config):
        self.data = None
        self.lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868, device_class = LoRa.CLASS_A)
        app_eui = ubinascii.unhexlify(config.staticConfiguration["appeui"])
        app_key = ubinascii.unhexlify(config.staticConfiguration["appkey"])
        self.lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0, dr=0)

        while not self.lora.has_joined():#replace by async
            time.sleep(2.5)
            print('Not yet joined...')
        print('joined')

    def send(self, msg): # TODO: optimise for power efficiency + check message lenght (with len(str.encode()) ?)
        """
        Send any buffer like objet to the LoRa network.
        """
        print("sending message with LoRa:" + msg)
        # create a LoRa socket
        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        # set the LoRaWAN data rate
        s.setsockopt(socket.SOL_LORA, socket.SO_DR, 0)
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        s.setblocking(True)

        s.send(msg)

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)

        # get any data received (if any...)
        self.data = s.recv(51)
        print("message sent")

    def hasMessage(self):
        if self.data is None:
            return False
        else:
            return True

    def getMessage(self):
        msg = self.data
        self.data = None
        return msg
