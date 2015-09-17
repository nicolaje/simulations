from morse.builder.creator import SensorCreator

class Keller(SensorCreator):
    _classpath = "eurathlon2015underwater.sensors.Keller.Keller"
    _blendname = "Keller"

    def __init__(self, name=None):
        SensorCreator.__init__(self, name)
