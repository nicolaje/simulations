import pymoos.MOOSCommClient
from morse.middleware.moos import AbstractMOOS


class TritechMicronPublisher(AbstractMOOS):

    _notified_sonar_connected = False

    def default(self, ci='unused'):
        cur_time = pymoos.MOOSCommClient.MOOSTime()
        if(not self._notified_sonar_connected):
            self._notified_sonar_connected=True
            self.m.Notify("SONAR_CONNECTED", "true", cur_time)
        self.m.Notify("SONAR_RAW_DATA","bearing="+str(self.data['incidence'])+",ad_interval=0,scanline=0",cur_time)
        self.m.Notify("SONAR_DISTANCE","bearing="+str(self.data['incidence'])+",distance="+str(self.data['range']),cur_time)
