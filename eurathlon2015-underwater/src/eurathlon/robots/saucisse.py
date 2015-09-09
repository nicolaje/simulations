import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.robot

class Saucisse(morse.core.robot.Robot):
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
    def __init__(self, obj, parent=None, sea_level=0, lever_arm_length=1, mf=(0.1**2)*3.14*1*1030, radius=0.1):
        logger.info('%s initialization' % obj.name)
        morse.core.robot.Robot.__init__(self, obj, parent)
        self._sea_level=sea_level
        self._lever_arm_length=lever_arm_length
        self._mf=mf
        self._radius=radius
        logger.info('Component initialized')

    def default_action(self):
        force=[self._u1+self._u2,0,self._u3]
        torque=[0,0,self._u2*self._lever_arm_length-self._u1*self._lever_arm_length]

        ## Compute an approximation of Archimedes force
        # If robot is underwater, apply Archimedes force
        # if robot is partially underwater, assumes Archimedes force varies linearly with its immersion
        delta = self.position_3d.z - self._sea_level
        if  delta <self._radius and delta > -self._radius:
            force[2]+=self.bge_object.mass*9.81*(1-delta/self._radius)/2
        elif self.position_3d.z - self._sea_level < -self._radius:
            force[2]+=1.1*self.bge_object.mass*9.81

        self.bge_object.applyForce(force,True)
        self.bge_object.applyTorque(torque,True)
