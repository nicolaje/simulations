import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.robot
from math import acos, sqrt
from morse.helpers.components import add_property

class Saucisse(morse.core.robot.Robot):
    add_property('_sea_level',0,'SeaLevel','float','Indicates the level of the sea. For example, if the mesh representing the sea is 0.7m above 0, set _sea_level=0')
    add_property('_lever_arm_length',1,'LeverArmLength','float','Distance from a thruster to the center of gravity of the robot. Does not apply to the vertical thruster')
    add_property('_mf',(0.1**2)*3.14*1*1030,'MF','float','Volume of the robot. Used to simulate Archimedes force.')
    add_property('_radius',0.1,'Radius','float','Radius of the cylinder of the robot in meter.')

    _name = 'saucisse robot'

    _u1 = 0 # Left thruster, looking forward (positive means turns right)
    _u2 = 0 # Right thruster, looking forward (positive means turns left)
    _u3 = 0 # Z-thruster, looking up (positive means go up)

    ##
    # sea_level : for example if the map is 1m too high, sea_level = 1
    # lever_arm_length : distance between a left/right thruster to the center of mass
    # mf : mass of the fluid displaced by the robot, used for Archimedes thrust, defaults to
    # the mass displaced by a cylinder of 20cm diameter, 1meter in length with a
    # water volumic mass of 1030 kg.m-3
    def __init__(self, obj, parent=None):
        logger.info('%s initialization' % obj.name)
        morse.core.robot.Robot.__init__(self, obj, parent)
        logger.info('Component initialized')
        print(self._sea_level)

    def default_action(self):
        force=[self._u1+self._u2,0,self._u3]
        torque=[0,0,self._u2*self._lever_arm_length-self._u1*self._lever_arm_length]

        ## Compute an approximation of Archimedes force
        # If robot is underwater, apply Archimedes force
        # if robot is partially underwater, assumes Archimedes force varies linearly with its immersion
        delta = self.position_3d.z - self._sea_level
        if  delta <self._radius and delta > -self._radius:
            h_imm=self._radius - delta
            vol_imm=self._radius**2*acos((self._radius-h_imm)/self._radius)-(self._radius-h_imm)*sqrt(2*self._radius*h_imm-h_imm**2)*1/(0.1**2*3.14*1)
            force[2]+=self.bge_object.mass*9.81
        elif self.position_3d.z - self._sea_level < -self._radius:
            force[2]+=1.01*self.bge_object.mass*9.81

        self.bge_object.applyForce(force,True)
        self.bge_object.applyTorque(torque,True)
