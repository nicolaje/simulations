import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.core import status
from morse.helpers.components import add_data, add_property

class Lejaunethruster(morse.core.actuator.Actuator):
    _name = "Lejaunethruster"
    _short_desc = "Propulseur pour le robot "

    add_data('u1', 0, 'float', 'Thruster force, positive means the boat goes forward')
    add_data('u2', 0, 'float', 'Thruster orientation, in degrees. 0 is neutral, 90 means the boat turns right, -90 means the boat turns left (the angle represents the rudder-stick angle with the x-axis of the robot.)')

    def __init__(self, obj, parent=None):
        morse.core.actuator.Actuator.__init__(self, obj, parent)

    def default_action(self):
        self.robot_parent._u1=self.local_data['u1']
        self.robot_parent._u2=self.local_data['u2']
