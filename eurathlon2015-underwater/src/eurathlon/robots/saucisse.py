import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.robot

class Saucisse(morse.core.robot.Robot):
    _name = 'saucisse robot'

    def __init__(self, obj, parent=None):
        logger.info('%s initialization' % obj.name)
        morse.core.robot.Robot.__init__(self, obj, parent)

        # Do here robot specific initializations
        logger.info('Component initialized')

    def default_action(self):
        pass
