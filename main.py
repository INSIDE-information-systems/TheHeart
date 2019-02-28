import GPS
import Network
import Memory
import Behaviour

gps = GPS.GPS() #GPS first to save time (fixing coordinates can be quite long)
configuration = Configuration.Configuration(Memory.restore()) # TODO: what if there is no configuration saved
network = Network.Network()
Behaviour.Behaviour(network, configuration)
