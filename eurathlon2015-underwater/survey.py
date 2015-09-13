#! /usr/bin/env morseexec
# In this mission, we acquire the elevation map with the
# Lejaune robot

from eurathlon.builder.robots import *
from eurathlon.builder.actuators import *
from eurathlon.builder.sensors import Tritechmicron
from morse.builder import *
from morse.helpers.coordinates import CoordinateConverter

jaune = Lejaune()
jaune.translate(x=0,y=-2,z=0.7)

tritech=Tritechmicron()
tritech.rotate(z=3.14/2)
jaune.append(tritech)

pose = Pose()
pose.add_stream('moos','eurathlon.sensors.customposepublisher.CustomPosePublisher',moos_port=9000)
jaune.append(pose)

velocity = Velocity()
jaune.append(velocity)

jauneactuator=Lejaunethruster()
jaune.append(jauneactuator)

# GPS
# On prend le point 0 en  lat= 42.95426460788653, lon=10.60175534337759,
# Ce qui correspond au coin sud-est de la pente de mise a l'eau des bateaux, en haut a gauche du port

gps=GPS()
#gps.properties(latitude=42.95426460788653,longitude=10.60175534337759,altitude=0)
gps.level('extended')
gps.add_stream('moos','eurathlon.sensors.gpspublisher.GPSPublisher',moos_port=9000)
jaune.append(gps)

jaune.add_default_interface('socket')

env = Environment('../data/eurathlon/environment/map.blend', fastmode = False)
env.set_camera_location([-18.0, 6, 10.8])
env.set_camera_rotation([1.09, 0, -3*3.14/4])
env.set_camera_clip(clip_start=0.1, clip_end=2000)
env.set_camera_speed(speed=4)
env.properties(longitude = 10.60175534337759, latitude = 42.95426460788653, altitude = 0)
