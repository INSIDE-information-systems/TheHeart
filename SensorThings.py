import ujson
from gpsUltimate import UltimateGPS
from Power import Power
import DriverManager

#La classe SensorThings sert à mettre en forme un message au format json utilisable par SensorThings API
class SensorThings :

#Fonction qui prend en paramètre un objet "gpsUltimate", dans lequel on va placer la valeur des coordonnées polaires
#coordonnées(latitute en °, longitude en °)
#La fonction retourne le message de position au format json pour sensorThings API
    def sensorthingify_location(location):
        msg_location = {
            "coordinates" : location
                }
        return ujson.dumps(msg_location)

#La fonction sensorthingify_observation met en forme un message d'observation au format json
    def sensorthingify_observation(measurement):
        battery = Power.getBattery()
        parameters = {
            "battery" : battery
        }

        msg_observation = {
            #"resultTime" : measurement.date, # TODO: rendre dynamique en fonction du driver l'envoi de la date
            "result" : measurement.value,
            "parameters" : parameters
        }
        return ujson.dumps(msg_observation)

#La fonction sensorThingify renvoie les messages qu'il y a à envoyer
#Soit que un message d'observation soit un message d'observation et un message de location
    def sensorThingify(measurement, sessionData):
        print("sensorThingify")
        msg_obs = SensorThings.sensorthingify_observation(measurement)
        if sessionData.lastGpsCoordinates is None:
            msg_loc = SensorThings.sensorthingify_location(measurement.location)
        else:
            if measurement.gpsInstance.isFixed():
                if(UltimateGPS.calculDistance(measurement.location[0],sessionData.lastGpsCoordinates[0],measurement.location[1],sessionData.lastGpsCoordinates[1])):
                    msg_loc = SensorThings.sensorthingify_location(measurement.location)
                else:
                    return [msg_obs]
            else:
                return [msg_obs]
        return [msg_loc,msg_obs]
