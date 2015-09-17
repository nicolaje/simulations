from morse.builder.creator import ActuatorCreator

class Lejaunethruster(ActuatorCreator):
    _classpath = "eurathlon2015underwater.actuators.lejaunethruster.Lejaunethruster"
    _blendname = "lejaunethruster"

    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name)
