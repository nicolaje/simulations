#! /usr/bin/env morseexec

from eurathlon.builder.robots import *
from eurathlon.builder.actuators import *
from morse.builder import *

robot = Lejaune()
saucisse = Saucisse()

robot.translate(1.0, 0.0, 0.7)
robot.rotate(0.0, 0.0, 3.5)

saucisse.translate(10,0,2.7)

robot.add_default_interface('socket')

env = Environment('map.blend', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
