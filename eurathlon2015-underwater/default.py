#! /usr/bin/env morseexec

from eurathlon.builder.robots import *
from eurathlon.builder.actuators import *
from morse.builder import *
import os

jaune = Lejaune()
saucisse = Saucisse()
saucisse.properties(SeaLevel=0.7)

jaune.translate(0, -2, 0.7)
jaune.rotate(0.0, 0.0, 0)

saucisse.translate(0,-3,-5)
saucisse.rotate(0,0,0)

jaune.add_default_interface('socket')
saucisse.add_default_interface('socket')

env = Environment('../data/eurathlon/environment/map.blend', fastmode = False)
env.set_camera_location([-18.0, 6, 10.8])
env.set_camera_rotation([1.09, 0, -3*3.14/4])
env.set_camera_clip(clip_start=0.1, clip_end=2000)
env.set_camera_speed(speed=4)
env.properties(longitude = 10.60175534337759, latitude = 42.95426460788653, altitude = 0)
