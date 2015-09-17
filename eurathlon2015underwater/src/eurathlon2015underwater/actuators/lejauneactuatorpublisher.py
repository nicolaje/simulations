import logging; logger = logging.getLogger("morse." + __name__)
import pymoos.MOOSCommClient
from morse.middleware.moos import AbstractMOOS

class LejauneReader(AbstractMOOS):
  def initialize(self):
    AbstractMOOS.initialize(self)
    self.m.Register("DESIRED_RUDDER")
    self.m.Register("DESIRED_THRUST")

  def default(self,ci='unused'):
    current_time=pymoos.MOOSCommClient.MOOSTime()
    messages=self.getRecentMail()

    new_information=False

    for message in messages:
      if (message.GetKey() == "DESIRED_RUDDER"):
        self.data['u1']=message.GetDouble()
        new_information=True
      elif(message.GetKey() == "DESIRED_THRUST"):
        self.data['u2']=message.GetDouble()
        new_information=True
    return new_information
