from morse.builder.creator import ActuatorCreator

class Saucisseactuator(ActuatorCreator):
    _classpath = "eurathlon2015underwater.actuators.saucisseactuator.Saucisseactuator"
    _blendname = "saucisseactuator"

    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name)
