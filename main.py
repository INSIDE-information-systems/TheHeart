import GPS
import Network
import Behaviour
import Measurement

gps = GPS.GPS() #GPS init first to save time (fixing coordinates can be quite long)
measurement = Measurement(gps)
configuration = Configuration.Configuration() # TODO: what if there is no configuration saved
network = Network.Network()
Behaviour.Behaviour(network, configuration, measurement)
