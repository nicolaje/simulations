import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.robot
from morse.helpers.components import add_property
from math import cos,sin,radians

class Lejaune(morse.core.robot.Robot):
    add_property('_lever_arm_length',0.3,'LeverArmLength','float','Distance from the center of mass of the boat to the thruster')

    _name = 'lejaune robot'

    _u1 = 0 # Thruster force, positive means the boat goes forward
    _u2 = 0 # Thruster orientation, in degrees. 0 is neutral, 90 means the boat turns right, -90 means the boat turns left (the angle represents the rudder-stick angle with the x-axis of the robot.)

    def __init__(self, obj, parent=None):
        logger.info('%s initialization' % obj.name)
        morse.core.robot.Robot.__init__(self, obj, parent)

        # Do here robot specific initializations
        logger.info('Component initialized')

    def default_action(self):
        self.bge_object.applyForce([self._u1*cos(radians(self._u2)),self._u1*sin(radians(self._u2)),0],True)
        self.bge_object.applyTorque([0,0,self._u1*sin(radians(self._u2))],True)
