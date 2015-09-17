#! /usr/bin/env python3

import time
import sys
import pymorse
import curses
import os
from datetime import datetime
from time import sleep
from pymorse import Morse
from math import cos,sin,radians,degrees,pi

readyToWrite=False
firstRun=True

pose_x = 0
pose_y = 0
posze_z = 0

yaw = 0

log = open("ranges.txt","w")

def update_pose(data):
    global pose_x
    global pose_y
    global pose_z
    global yaw

    pose_x=data['x']
    pose_y=data['y']
    pose_z=data['z']
    yaw=data['yaw']

def update_sonar(data):
    log.write("NODE "+str(pose_x)+" "+str(pose_y)+" "+str(posze_z)+" 0 0 "+str(yaw)+"\n"+\
    str(pose_x+data['range']*cos(yaw-radians(90))*cos(-pi+radians(data['incidence'])))+" "+\
    str(pose_y+data['range']*sin(yaw-radians(90))*cos(-pi+radians(data['incidence'])))+" "+\
    str(pose_z-sin(radians(-pi+data['incidence']))*data['range'])+'\n')
    print("incidence: "+str(data['incidence']))
    print("range: "+str(data['range']))
    print("x: "+str(pose_x))
    print("y: "+str(pose_y))
    print("z: "+str(pose_z))
    print("yaw: "+str(degrees(yaw)))
    print("Endpoint: "+\
    str(pose_x+data['range']*cos(yaw-radians(90))*cos(-pi+radians(data['incidence'])))+" "+\
    str(pose_y+data['range']*sin(yaw-radians(90))*cos(-pi+radians(data['incidence'])))+" "+\
    str(pose_z-sin(radians(-pi+data['incidence']))*data['range']))
    log.flush()

s = Morse()

s.jaune.pose.subscribe(update_pose)
s.jaune.tritech.subscribe(update_sonar)
