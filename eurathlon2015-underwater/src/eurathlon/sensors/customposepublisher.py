import pymoos.MOOSCommClient
from morse.middleware.moos import AbstractMOOS
from math import sqrt

class CustomPosePublisher(AbstractMOOS):

    def default(self, ci='unused'):
        cur_time = pymoos.MOOSCommClient.MOOSTime()
        self.m.Notify("GPS_E",str(self.data['x']),cur_time)
        self.m.Notify("GPS_N",str(self.data['y']),cur_time)
        self.m.Notify("GPS_ALTITUDE",str(self.data['z']),cur_time)
