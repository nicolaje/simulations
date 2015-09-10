#! /usr/bin/env morseexec

from eurathlon.builder.robots import *
from eurathlon.builder.actuators import *
from morse.builder import *
import os

jaune = Lejaune()
saucisse = Saucisse()
saucisse.properties(SeaLevel=0.7)

jaune.translate(1.0, 0.0, 0.7)
jaune.rotate(0.0, 0.0, 0)

saucisse.translate(10,0,0.7)
saucisse.rotate(0,0,0)

jaune.add_default_interface('socket')
saucisse.add_default_interface('socket')

env = Environment('../data/eurathlon/environment/map.blend', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
