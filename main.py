import gpsUltimate
import Network
import Behaviour
import Measurement
import SessionData
from DriverManager import DriverManager

gps = gpsUltimate.UltimateGPS() #GPS init first to save time (fixing coordinates can be quite long)
driverManger = DriverManager()
measurement = Measurement.Measurement(gps, driverManger)
data = SessionData.SessionData() 
network = Network.Network(data)
Behaviour.Behaviour(network, data, measurement)
