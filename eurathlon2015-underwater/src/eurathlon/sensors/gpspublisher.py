import pymoos.MOOSCommClient
from morse.middleware.moos import AbstractMOOS
from math import sqrt

class GPSPublisher(AbstractMOOS):

    def default(self, ci='unused'):
        cur_time = pymoos.MOOSCommClient.MOOSTime()
        self.m.Notify("GPS_TIME",str(self.data['time']),cur_time)
        self.m.Notify("GPS_SPEED",str(sqrt(self.data['velocity'][0]**2+self.data['velocity'][1]**2+self.data['velocity'][2]**2)),cur_time)
        self.m.Notify("GPS_HEADING",str(self.data['heading']),cur_time)
        self.m.Notify("GPS_YAW",str(90-self.data['heading']),cur_time)
        #self.m.Notify("GPS_E",str(self.position_3d.x),cur_time)
        #self.m.Notify("GPS_N",str(self.position_3d.y),cur_time)
        #self.m.Notify("GPS_ALTITUDE",str(self.position_3d.z),cur_time)
        self.m.Notify("GPS_LONGITUDE",str(self.data['longitude']),cur_time)
        self.m.Notify("GPS_LATITUDE",str(self.data['latitude']),cur_time)
        self.m.Notify("GPS_NB_SAT","42",cur_time)
