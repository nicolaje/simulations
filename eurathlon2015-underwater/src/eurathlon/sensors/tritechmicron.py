import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.sensor

from morse.core.services import service, async_service
from morse.core import status
from morse.helpers.components import add_data, add_property
from morse.sensors.laserscanner import LaserScanner

class Tritechmicron(LaserScanner):
    """Write here the general documentation of your sensor.
    It will appear in the generated online documentation.
    """

    _name = "Tritechmicron"
    _short_desc = "Simulator for the Tritech Micron sonar"
    -rot = 0

    # define here the data fields exported by your sensor
    # format is: field name, default initial value, type, description
    add_data('distance', 0.0, 'float', 'A dummy odometer, for testing purposes. Distance in meters')
    add_data('color', 'none', 'str', 'A dummy colorimeter, for testing purposes. Default to \'none\'.')

    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        LaserScanner.__init__(self, obj, parent)

        # Do here sensor specific initializations

        self._distance = 0 # dummy internal variable, for testing purposes

        logger.info('Component initialized')
        print("SALUT C'EST COOL")

    @service
    def get_current_distance(self):
        """ This is a sample (blocking) service (use 'async_service' decorator
        for non-blocking ones).

        Simply returns the value of the internal counter.

        You can access it as a RPC service from clients.
        """
        logger.info("%s is %sm away" % (self.name, self.local_data['distance']))

        return self.local_data['distance']

    """Used for Velodyne sensor"""
    def default_action(self):
        LaserScanner.default_action(self)
        self.applyRotationZ()


    def applyRotationZ(self, rz=.01745):
        # The second parameter specifies a "local" movement
        self.bge_object.applyRotation([0, rz, 0], True)
