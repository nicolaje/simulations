from morse.builder import *

class Saucisse(GroundRobot):
    """
    A template robot model for saucisse, with a motion controller and a pose sensor.
    """
    def __init__(self, name = None, debug = True):

        # saucisse.blend is located in the data/robots directory
        GroundRobot.__init__(self, 'eurathlon2015underwater/robots/saucisse.blend', name)
        self.properties(classpath = "eurathlon2015underwater.robots.saucisse.Saucisse")
