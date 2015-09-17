#! /usr/bin/env python3

import sys
import curses
import os

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

s = Morse()

u1 = 0
u2 = 0

position=0
linear_speed=0
angular_speed=0

position = 0

def pose_received(p):
    global position
    position=p

def speed_received(s):
    global linear_speed
    global angular_speed
    linear_speed=s["linear_velocity"]
    angular_speed=s["angular_velocity"]

jauneactuator = s.jaune.jauneactuator
s.jaune.pose.subscribe(pose_received)
s.jaune.velocity.subscribe(speed_received)

def run(win):
    win.timeout(100)
    doRun=True
    while doRun:
        global jauneactuator
        global duration
        global u1
        global u2
        win.addstr(0, 0, "Arrow Up/Down Keys to accelerate/decelerate")
        win.addstr(1, 0, "Arrow Left/Right Keys to turn left/right")
        if position != 0 and linear_speed !=0 and angular_speed != 0 :
            win.addstr(2, 0, "Position: ")
            win.addstr(2, 15, '['+"{0:.2f}".format(position['x'])+", "+\
            "{0:.2f}".format(position['y'])+\
            ", "+"{0:.2f}".format(position['z'])+']')
            win.addstr(3, 0, "Orientation: ")
            win.addstr(3, 15, '['+"{0:.2f}".format(position['roll'])+", "+\
            "{0:.2f}".format(position['pitch'])+", "+\
            "{0:.2f}".format(position['yaw'])+']')
            win.addstr(4, 0, "Linear Speed: ")
            win.addstr(4, 15, '['+"{0:.2f}".format(linear_speed[0])+", "+\
            "{0:.2f}".format(linear_speed[1])+", "+\
            "{0:.2f}".format(linear_speed[2])+']')
            win.addstr(5, 0, "Angular Speed: ")
            win.addstr(5, 15, '['+"{0:.2f}".format(angular_speed[0])+", "+\
            "{0:.2f}".format(angular_speed[1])+", "+\
            "{0:.2f}".format(angular_speed[2])+']')
            win.addstr(7,0,"Press q to quit.")

            c = win.getch()
            if c == curses.KEY_UP  :
                u1+=0.1
            elif c == curses.KEY_DOWN :
                u1-=0.1
            elif c == curses.KEY_LEFT :
                u2+=1 # +1 degree should be enough
            elif c == curses.KEY_RIGHT :
                u2-=1
            elif c == 113:
                doRun=False
            jauneactuator.publish({'u1':u1,'u2':u2})

curses.wrapper(run)
