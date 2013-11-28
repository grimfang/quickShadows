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

Start the MeoTech Engine.
"""

# System Imports
import logging as log

# Panda Engine Imports
from panda3d.bullet import BulletWorld, BulletDebugNode
from panda3d.core import Vec3

# MeoTech Imports
from factory import Factory
from config import *

#----------------------------------------------------------------------#

# Engine
class Engine():
    """The engine handles the building and setup of the level, every
    thing parsed from the level.egg.
    """
    def __init__(self, _meotech):
        
        print "Engine - init >>>"
        
        # MeoTehc
        self.meotech = _meotech
        
        ### Setup Engine Holders ###
        
        # Create Game Object Holders
        self.GameObjects = {}
        self.GameObjects["player"] = None
        self.GameObjects["level"] = {}
        self.GameObjects["object"] = {}
        self.GameObjects["light"] = {}
        self.GameObjects["sensor"] = {}
        
        # Create Render Object Holders for sorting stuff in sceneG.
        # nodepaths
        self.RenderObjects = {}
        self.BulletObjects = {}
        
        # none visual
        self.BulletObjects["main"] = render.attachNewNode("Bullet_main")
        self.BulletObjects["player"] = self.BulletObjects["main"].attachNewNode("Bullet_player")
        self.BulletObjects["level"] = self.BulletObjects["main"].attachNewNode("Bullet_level")
        self.BulletObjects["object"] = self.BulletObjects["main"].attachNewNode("Bullet_object")
        self.BulletObjects["sensor"] = self.BulletObjects["main"].attachNewNode("Bullet_sensor")
        
        # Visuals
        self.RenderObjects["level"] = render.attachNewNode("Render_level")
        self.RenderObjects["object"] = render.attachNewNode("Render_object")
        self.RenderObjects["light"] = render.attachNewNode("Render_light")
        
        ### Engine Holders END ###
        
        # Setup Bullet Physics
        self.bulletWorld = BulletWorld()
        self.bulletWorld.setGravity(Vec3(GRAVITY_X, GRAVITY_Y, GRAVITY_Z))
        
        # Init Factory
        self.factory = Factory(self)
        self.factory.parseLevelFile("test")
        
        # Init Input
        
        # Start Engine Loop
        # Controls Physics and other engine related Things
        taskMgr.add(self.engineLoop, "Engine_Loop")
        
    
    def showBulletDebug(self):
        """Show bullet Debug"""
        # Bullet DEBUG
        debugNode = BulletDebugNode('Debug')
        debugNode.showWireframe(True)
        debugNode.showConstraints(True)
        debugNode.showBoundingBoxes(False)
        debugNode.showNormals(False)
        debugNP = render.attachNewNode(debugNode)
        debugNP.show()
        
        self.bulletWorld.setDebugNode(debugNP.node())
        
    
    def engineLoop(self, task):
        """Handle Engine Related Tasks"""
        dt = globalClock.getDt()
        
        # Handle Physics
        self.bulletWorld.doPhysics(dt)
        
        return task.cont


















