#! /usr/bin/env morseexec
# In this mission, we acquire the elevation map with the
# Lejaune robot

from eurathlon.builder.robots import *
from eurathlon.builder.actuators import *
from eurathlon.builder.sensors import Tritechmicron
from morse.builder import *

jaune = Lejaune()
jaune.translate(x=-150,y=300,z=0.7)

tritech=Tritechmicron()
tritech.rotate(z=3.14/2)
jaune.append(tritech)

pose = Pose()
jaune.append(pose)

velocity = Velocity()
jaune.append(velocity)

jauneactuator=Lejaunethruster()
jaune.append(jauneactuator)

jaune.add_default_interface('socket')

env = Environment('../data/eurathlon/environment/map.blend', fastmode = False)
env.set_camera_location([-18.0-150, -6.7+330, 10.8])
env.set_camera_rotation([1.09, 0, -3*3.14/4])
env.set_camera_clip(clip_start=0.1, clip_end=2000)
env.set_camera_speed(speed=4)
