from morse.builder import *

class Lejaune(GroundRobot):
    """
    A template robot model for lejaune, with a motion controller and a pose sensor.
    """
    def __init__(self, name = None, debug = True):

        # lejaune.blend is located in the data/robots directory
        GroundRobot.__init__(self, 'eurathlon/robots/lejaune.blend', name)
        self.properties(classpath = "eurathlon.robots.lejaune.Lejaune")
