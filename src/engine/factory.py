#!/usr/bin/python

################
# The MIT License (MIT)
#
# Copyright (c) <2013> <Martin de Bruyn>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
############################################################

#----------------------------------------------------------------------#

"""@ package MeoTech

Start the Engine Factory.
"""

# System Imports
import logging as log

# Panda Engine Imports
from panda3d.core import NodePath

# MeoTech Imports
from config import *
from basePhysics import BasePhysics
from baseObject import BasePlayer, BaseLevel, BaseLight

#----------------------------------------------------------------------#

# Factory
class Factory():
    """The factory handles the building of levels and all the objects,
    lights, sensors... in them.
    """
    def __init__(self, _engine):
        
        print "Factory - init >>>"
        
        # Engine
        self.engine = _engine
        
        # BasePhysics keeper of things
        self.basePhysics = BasePhysics(self.engine)
        
    def parseLevelFile(self, _eggPath):
        
        # Egg file
        levelEgg = loader.loadModel(LEVEL_DIR + _eggPath)
        
        # Find objects in levelEgg
        levelObjects = levelEgg.findAllMatches('**')
        
        for obj in levelObjects:
            for type in OBJECT_TYPES:
                
                if obj.hasTag(type):
                    self.buildObject(type, obj, levelEgg)
                    
    
    def buildObject(self, _type, _obj, _levelEgg):
        
        # Build Object with _type
        
        # Player Type
        if _type == "player":
            self.engine.GameObjects["player"] = BasePlayer(self.engine,
                            _type, _obj, _levelEgg)
        
        # Level Type
        if _type == "level":
            self.engine.GameObjects["level"][_obj.getTag("level")] = BaseLevel(self.engine, 
                            _type, _obj, _levelEgg)
            
        # Object Type
        if _type == "object":
            self.engine.GameObjects["object"][_obj.getTag("object")] = BaseObject()
            
        # Light Type
        if _type == "light":
            self.engine.GameObjects["light"][_obj.getTag("light")] = BaseLight(
                            self.engine, _type, _obj, _levelEgg)
            
        # Sensor Type
        if _type == "sensor":
            self.engine.GameObjects["sensor"][_obj.getTag("sensor")] = BaseSensor()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
