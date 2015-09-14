import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.sensor

from morse.core.services import service, async_service
from morse.core import status
from morse.helpers.components import add_data, add_property
from morse.sensors.laserscanner import LaserScanner
from morse.builder import bpymorse
from math import radians
from numpy import mean
import bpy

class Tritechmicron(LaserScanner):
    """Write here the general documentation of your sensor.
    It will appear in the generated online documentation.
    """

    _name = "Tritechmicron"
    _short_desc = "Simulator for the Tritech Micron sonar"
    _rot = 0

    add_data('range', 0.0, 'float', 'Range detected by the sonar. It is the mean range of the range_list data.')
    add_data('incidence', 0.0, 'float', 'Incidence of the beam that measured the range. ')

    add_property('angle_per_ping',6,'angle_per_ping',"float","The angle jump between two pings, in degrees.")
    add_property('scan_coverage',120,'scan_coverage',"float","The width of the zone to be covered by the sonar, in degrees.")

    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        LaserScanner.__init__(self, obj, parent)
        self.bge_object.applyRotation([0,radians(90-self.scan_coverage/2),0],True)
        #arcMat=None
        #if 'RayMat' in bpymorse.get_materials():
        #    m = bpymorse.get_material('RayMat')
        #    print(str(type(bpymorse.get_material('RayMat'))))
        #    print(str(dir(bpymorse.get_material('RayMat'))))
        #    print("m.game_settings.use_backface_culling: "+str(m.game_settings.use_backface_culling))
        #    m.game_settings.use_backface_culling= False
        #    print("m.game_settings.use_backface_culling: "+str(m.game_settings.use_backface_culling))
        #    arcMat= m
        #m.diffuse_color=(0,0,1)
        #m.use_transparency=False
        #arcName = ""
        #for child in obj.children:
        #    print(child.name)
        #    if "Arc_" in child.name:
        #        print(child.name + "contains Arc_")
        #        arcName=child.name
        #arcObj=bpymorse.get_object(arcName)
        #bpymorse.select_only(arcObj)
        #bpy.ops.object.modifier_add(type='SOLIDIFY')
        #print("str(dir(arcObj)): "+str(dir(arcObj)))
        #print("str(dir(arcObj.data)): "+str(dir(arcObj.data)))
        #print("arcObj.data.show_double_sided : "+str(arcObj.data.show_double_sided))
        #print("self.local_data.keys(): "+str(self.local_data.keys()))
        #        print(str(dir(child)))
        #        print(dir(child.meshes))
        #        print(len(child.meshes))
        #        print(str(dir(child.meshes[0])))
        #        print(child.meshes[0].getMaterialName(0))
        #        print(len(child.meshes[0].materials))
        #        #print(child.meshes[0].materials.name)
        #        print(str(dir(child.meshes[0].materials[0])))

    def default_action(self):
        LaserScanner.default_action(self)
        self.local_data['range']=mean(self.local_data['range_list'])
        self.local_data['incidence']=self._rot+90-self.scan_coverage/2
        self.bge_object.applyRotation([0,radians(self.angle_per_ping),0],True)
        self._rot+=self.angle_per_ping
        if self._rot > self.scan_coverage :
            self.bge_object.applyRotation([0,-radians(self._rot),0],True)
            self._rot = 0
