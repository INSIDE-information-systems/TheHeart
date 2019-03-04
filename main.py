import gpsUltimate
import Network
import Behaviour
import Measurement
import SessionData

gps = gpsUltimate.UltimateGPS() #GPS init first to save time (fixing coordinates can be quite long)
measurement = Measurement.Measurement(gps)
data = SessionData.SessionData() # TODO: what if there is no configuration saved
network = Network.Network(data)
Behaviour.Behaviour(network, data, measurement)
