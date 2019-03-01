import ujson
import gpsUltimate
import Power
import DriverManager

#La classe SensorThings sert à mettre en forme un message au format json utilisable par SensorThings API
class SensorThings :

#Fonction qui prend en paramètre un objet "GPS", dans lequel on va placer la valeur des coordonnées polaires
#coordonnées(latitute en °, longitude en °)
#La fonction retourne le message de position au format json pour sensorThings API
    def sensorthingify_location(gps):
        msg_location = {
            #"coordinates" : gps
            "coordinates" : gps.getLocation()
                }
        return ujson.dumps(msg_location)


#Fonction qui prend en paramètre un objet "GPS", un objet "battery" et un objet "value"
#Dans lesquels on va placer respectivement la date et l'heure renvoyées par le module gps
#Une estimation de la valeur de la batterie du The+Heart
#Et enfin la valeur du capteur I2C branché
#La fonction retourne le message de l'observation au format json pour sensorThings API
    def sensorthingify_observation(gps, battery, value):
        parameters = {
        "battery" : battery.getBattery
        #"battery" : battery
        }

        msg_observation = {
            "resultTime" : gps.getTime,
            #"resultTime" : gps,
            "result" : value.getValue,
            "parameters" : parameters
        }
        #print(msg)
        return ujson.dumps(msg_observation)

    def sensorThingify():
        updateLocation = UltimateGPS.UltimateGPS.calculDistance()
        msg_obs = SensorThings.SensorThings.sensorthingify_observation()

        if(updateLocation>=5):
            msg_loc = SensorThings.SensorThings.sensorthingify_location()
            return message = [msg_loc,msg_obs]
        elif:
            return message = [msg_obs]
