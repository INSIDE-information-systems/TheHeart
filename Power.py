from machine import Pin

class Power :

    vbatPin = 32

    def getBattery():

        #On va lire la pin sur laquelle on a branché la batterie (en Volt)
        voltageBattery = Pin(vbatPin, Pin.IN)

        #Si la tention lue est comprise entre 3 et 3,7 V
        #On utilise la formule y=(0.06*x) + 3 avec x la valeur en Volt lue sur la pin
        #Et y la valeur en % de la batterie
        #Les équations sont trouvées à partir de l'estimation de la courbe de décharge de la batterie

        if(voltageBattery>=3 and voltageBattery<=3.7):
            battery = (0.06*VoltageBattery) + 3

        #Si la tention lue est comprise entre 3,7 et 3,97 V
        #On utilise la formule y = (0.0044*x) + 3.612 avec x la valeur en Volt lue sur la pin
        #Et y la valeur en % de la batterie
        elif(voltageBattery>3.7 and voltageBattery<=3.97):
            battery = (0.0044*x) + 3.612

        #Si la tention lue est comprise entre 3,97 et 4,2 V
        #On utilise la formule y = (0.0115*x) + 3.05 avec x la valeur en Volt lue sur la pin
        #Et y la valeur en % de la batterie
        elif(voltageBattery>3.97 and voltageBattery<=4.2):

            battery = (0.0115*x) + 3.05
            
        return battery
