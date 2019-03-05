import machine

class Power :

    def getBattery():

        gpio = 32 #Numero de la GPIO sur laquelle est branchée la batterie sur l'esp32

        #On va lire la pin sur laquelle on a branché la batterie (en Volt)

        #for esp32:
        # adc_pin = machine.Pin(32)
        # adc = machine.ADC(adc_pin)
        # voltageBattery = adc.read()
        #voltageBattery = voltageBattery * (1 / 4095)

        #for pycom:
        adc = machine.ADC()
        apin = adc.channel(pin='P18')
        voltageBattery = apin.voltage()/1000*4.14

        if(voltageBattery<3):
            battery = 0

        #Si la tention est comprise entre 3 et 3,7 V
        #On utilise la formule y=(0.06*x) + 3 avec y la valeur en Volt et x la valeur en % de la batterie
        #Les équations sont trouvées à partir de l'estimation de la courbe de décharge de la batterie
        elif(voltageBattery>=3 and voltageBattery<=3.7):
            battery = (voltageBattery - 3)/0.06

        #Si la tention lue est comprise entre 3,7 et 3,97 V
        #On utilise la formule y = (0.0044*x) + 3.612 avec y la valeur en Volt et x la valeur en % de la batterie
        elif(voltageBattery>3.7 and voltageBattery<=3.97):
            battery = (voltageBattery - 3.612)/0.0044

        #Si la tention lue est comprise entre 3,97 et 4,2 V
        #On utilise la formule y = (0.0115*x) + 3.05 avec y la valeur en Volt et x la valeur en % de la batterie
        elif(voltageBattery>3.97 and voltageBattery<=4.2):
            battery = (voltageBattery - 3.05)/0.0115

        elif(voltageBattery>4.2):
            battery = 100

        print(voltageBattery)
        return battery
