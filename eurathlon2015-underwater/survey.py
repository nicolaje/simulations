#! /usr/bin/env morseexec
# In this mission, we acquire the elevation map with the
# Lejaune robot

from eurathlon.builder.robots import *
from eurathlon.builder.actuators import *
from eurathlon.builder.sensors import Tritechmicron
from morse.builder import *

jaune = Lejaune()
jaune.translate(z=0.7)
#ir = Infrared()
#ir.properties(laser_range=50)
#jaune.append(ir)
tritech=Tritechmicron()
tritech.translate(z=2)
tritech.rotate(z=3.14/2)
jaune.append(tritech)

env = Environment('../data/eurathlon/environment/map.blend', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
