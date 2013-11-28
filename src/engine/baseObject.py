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

"""@ package BaseObject

Classes for the BaseObjects types.
Each type of object from the level.egg file will be build from these.
"""

# System Imports
import logging as log

# Panda Engine Imports
from panda3d.core import PointLight, DirectionalLight, Spotlight, AmbientLight
from panda3d.core import VBase4, PerspectiveLens

# MeoTech Imports
from config import *

#----------------------------------------------------------------------#

# BaseObject Types

# BasePlayer
class BasePlayer():
    """
    BasePlayer:
    This builds a player character.
    """
    def __init__(self, _engine, _type, _obj, _levelEgg):
        """BasePlayer Contructor"""
        print "start buidling: ", _obj, " Type: ", _type
        
        # Engine
        self.engine = _engine
        self.factory = self.engine.factory
        
        # Object
        self.object = _obj
        
        # Get the tags from the object
        self.name = _obj.getTag("player")
        self.id = int(_obj.getTag("id"))
        self.control = _obj.getTag("controlType")
        self.model = _obj.getTag("model")
        self.height = float(_obj.getTag("height"))
        self.radius = float(_obj.getTag("radius"))
        self.runSpeed = float(_obj.getTag("runSpeed"))
        self.walkSpeed = float(_obj.getTag("walkSpeed"))
        self.turnSpeed = float(_obj.getTag("turnSpeed"))
        #self.jumpHeight = float(_obj.getTag("jumpHeight"))
        self.isDynamic = _obj.getTag("isDynamic")
        self.script = _obj.getTag("script")
        
        # States
        self.position = _obj.getPos(_levelEgg)
        self.heading = _obj.getH(_levelEgg)
        
        # Player Collision Body
        self.bulletBody = None
        self.useBasicMovement = False
        
        # Run checkers
        self.setControlType()
        self.setModel()
        # TODO: Load scripts for this object...
        
        # Log
        log.debug("Player Builder build: %s" % (self.name))
    
    
    def setControlType(self):
        
        # Check Fps Style
        if self.control == "controlType0":
            """Add a Fps Type cam and controller"""
            # Add character controler from bullet
            # Add the fps style camera
            self.bulletBody = self.factory.basePhysics.buildCharacterController(
                        self.height, self.radius, self.position, self.heading)
            
            self.useBasicMovement = True
            # camera go here..
            
        # Check 3rd Person Style
        if self.control == "controlType1":
            """Add a 3rd Person view cam and controller"""
            # Add Character controller from bullet
            # Add the 3rd Person view Camera
            pass
            
        # Check rpg style camera
        if self.control == "controlType2":
            """Add a rpg top down style camera"""
            # Add camera
            # add the basic controller same as fps
            # replace this style with more options to support 
            # point and click style movement aswell.
            pass
            
        # Check side scroller type camera
        if self.control == "controlType3":
            """Add a side scroller style camera"""
            # Add a side scroller type camera
            pass
    
    def setModel(self):
        """Attach the given model to the player"""
        if self.model != "":
            # Setup the visual model
            # Animated stuff should be added soon
            model = loader.loadModel(MODEL_DIR + self.model)
            model.reparentTo(self.bulletBody)


# BaseLevel
class BaseLevel():
    """THis builds the level parts, floor, walls
    TODO: add water functionality with shaders"""
    def __init__(self, _engine, _type, _obj, _levelEgg):
        """BaseLevel Constructor"""
        print "start building: ", _obj, " Type: ", _type
        
        # Engine
        self.engine = _engine
        self.factory = self.engine.factory
        self.renderObjectsLevel = self.engine.RenderObjects["level"]
        self.levelEgg = _levelEgg
        
        # Object
        self.object = _obj
        
        # Get the tags from the object
        self.name = _obj.getTag("level")
        self.id = int(_obj.getTag("id"))
        self.subType = _obj.getTag("subType")
        self.isDynamic = _obj.getTag("isDynamic")
        self.useBulletPlane = _obj.getTag("useBulletPlane")
        self.script = _obj.getTag("script")
        
        # States
        self.position = _obj.getPos(_levelEgg)
        self.hpr = _obj.getHpr(_levelEgg)
        self.scale = _obj.getScale(_levelEgg)
        
        # CollisionBody
        self.bulletBody = None
        
        # Run Checkers
        self.buildSubType()
        
        # Log
        log.debug("Level Builder build: %s" % (self.name))
        
    def buildSubType(self):
        """Build the subType that being either wall or ground"""
        
        if self.subType == "wallType":
            """Build a wall"""
            
            if "col" in self.name:
                """Build the collision body for this wall"""
                self.bulletBody = self.factory.basePhysics.buildTriangleMesh(
                            self.object, self.levelEgg, 0, self.isDynamic)
            
            else:
                self.object.reparentTo(self.renderObjectsLevel)
        
        elif self.subType == "groundType":
            """Build the ground with either custom Mesh or use the plane"""
            if self.useBulletPlane:
                self.factory.basePhysics.buildGroundPlane()
                
                self.object.reparentTo(self.renderObjectsLevel)
                self.object.setPos(self.position)
                self.object.setHpr(self.hpr)
            
            else:
                
                if "col" in self.name:
                    self.bulletBody = self.factory.basePhysics.buildTriangleMesh(
                            self.object, self.levelEgg, 0, self.isDynamic)
                
                else:
                    self.object.reparentTo(self.renderObjectsLevel)
                    self.object.setPos(self.position)
                    self.object.setHpr(self.hpr)


# BaseLight
class BaseLight():
    """BaseLight:
    Make some lights :)
    """
    def __init__(self, _engine, _type, _obj, _levelEgg):
        """BaseLights Constructor"""
        print "start building: ", _obj, " Type: ", _type
        
        # Engine
        self.engine = _engine
        self.factory = self.engine.factory
        self.renderObjectsLight = self.engine.RenderObjects["light"]
        
        # Object
        self.object = _obj
        
        # get the tags from the object
        self.name = _obj.getTag("light")
        self.id = int(_obj.getTag("id"))
        self.subType = _obj.getTag("subType")
        self.model = _obj.getTag("model")
        self.isDynamic = _obj.getTag("isDynamic")
        self.script = _obj.getTag("script")
        self.color = self.getColor(_obj.getTag("color"))
        self.lookAt = _obj.getTag("lookAt")
        
        # NodePath
        self.lightNP = None
        
        # States
        self.position = _obj.getPos(_levelEgg)
        self.hpr = _obj.getHpr(_levelEgg)
        self.h = _obj.getH(_levelEgg)
        
        # Run Checkers
        self.buildSubType()
        # Log
    
    def buildSubType(self):
        """Build the light with the given subType"""
        
        if self.subType == "pointType":
            # make a point light
            c = self.color
            pointLight = PointLight(self.name)
            pointLight.setColor(VBase4(c[0], c[1], c[2], c[3]))
            plnp = self.renderObjectsLight.attachNewNode(pointLight)
            plnp.setPos(self.position)
            self.lightNP = plnp
            self.setLightSwitch(True)
            
        if self.subType == "directType":
            # make a directional light
            c = self.color
            directLight = DirectionalLight(self.name)
            directLight.setColor(VBase4(c[0], c[1], c[2], c[3]))
            dlnp = self.renderObjectsLight.attachNewNode(directLight)
            dlnp.setHpr(0, -60, 0) # no idea why its like that.. but it works
            self.lightNP = dlnp
            self.setLightSwitch(True)
            
            
        if self.subType == "ambientType":
            # make a ambient light
            c = self.color
            ambientLight = AmbientLight(self.name)
            ambientLight.setColor(VBase4(c[0], c[1],c[2], c[3]))
            alnp = self.renderObjectsLight.attachNewNode(ambientLight)
            self.lightNP = alnp
            self.setLightSwitch(True)
            
        if self.subType == "spotType":
            # make a spot light
            # lookAtObj = _object.getTag("lookAt") get rid of this.
            c = self.color
            spotLight = Spotlight(self.name)
            spotLight.setColor(VBase4(c[0], c[1], c[2], c[3]))
            lens = PerspectiveLens()
            spotLight.setLens(lens)
            slnp = self.renderObjectsLight.attachNewNode(spotLight)
            slnp.setPos(self.position)
            slnp.setHpr(self.hpr)
            # Find out if this is really the only option
            # because setHpr doesnt seem to have any effect.
            # lookAt would be okay but that means adding anothe type
            #slnp.lookAt(self.main.GameObjects["player"].collisionBody)
            self.lightNP = slnp
            self.setLightSwitch(True)
    
    def getColor(self, _color):
        """Get the color and convert it from the string tag"""
        c = _color.split()
        
        for n in range(len(c)):
            c[n] = float(c[n])
        
        return c
        
    def setLightSwitch(self, _state=False):
        """Set the light on or off."""
        if _state == True:
            render.setLight(self.lightNP)
        elif _state == False:
            render.clearLight(self.lightNP)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
