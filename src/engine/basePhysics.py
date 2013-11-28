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

"""@ package BasePhysics

All Physics setups and builders
"""

# System Imports
import logging as log

# Panda Engine Imports
from panda3d.bullet import BulletCharacterControllerNode
from panda3d.bullet import BulletCapsuleShape
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletTriangleMesh, BulletTriangleMeshShape
from panda3d.bullet import ZUp
from panda3d.core import Vec3, BitMask32
from direct.showbase.InputStateGlobal import inputState

# MeoTech Imports

#----------------------------------------------------------------------#

# BasePhysics
class BasePhysics():
    """Holds all Physics related builders and setups stuff"""
    def __init__(self, _engine):
        
        # Engine
        self.engine = _engine
        
        # Player state stuff
        self.crouching = False
    
    def buildGroundPlane(self):
        """Build a BulletPlane"""
        shape = BulletPlaneShape(Vec3(0, 0, 1), 0)
        np = self.engine.BulletObjects["level"].attachNewNode(
                                    BulletRigidBodyNode('Ground_plane'))
        np.node().addShape(shape)
        np.setPos(0, 0, 0) # This thing is usually infinite
        np.setCollideMask(BitMask32.allOn())
        
        self.engine.bulletWorld.attachRigidBody(np.node())
        
    def buildCharacterController(self, _height, _radius, _pos, _head):
        """Build a basic BulletCharacter Controller"""
        shape = BulletCapsuleShape(_radius, _height-2 * _radius, ZUp)
        
        charNode = BulletCharacterControllerNode(shape, _radius, "Player")
        np = self.engine.BulletObjects["player"].attachNewNode(charNode)
        np.setPos(_pos)
        np.setH(_head)
        np.setCollideMask(BitMask32.allOn())
        
        self.engine.bulletWorld.attachCharacter(np.node())
        return np
        
    def doPlayerJump(self, player):
        """Allow the player to perform a jump"""
        
        # set jump height, speed
        player.setMaxJumpHeight(5.0)
        player.setJumpSpeed(8.0)
        player.doJump()
        
    
    def doPlayerCrouch(self, player):
        """Allow the player to perform crouch"""
        self.crouching = not self.crouching
        
        sz = self.crouching and 0.6 or 1.0
        #player.bulletBody.node().getShape().setLocalScale(Vec3(1, 1, sz))
        
        # Get the player nodepath
        player.bulletBody.setScale(Vec3(1, 1, sz))# * 0.3048)
        #player.setPos(0, 0, -1 * sz)
    
        
    def useBasicPlayerMovement(self, dt):
        """This sets up a basic movement for the playercontroller"""
        
        # get the player
        player = self.engine.GameObjects["player"]
        speed = Vec3(0, 0, 0)
        omega = 0.0
        
        if inputState.isSet('forward'): speed.setY(player.runSpeed)
        if inputState.isSet('reverse'): speed.setY(-player.runSpeed)
        if inputState.isSet('left'): speed.setX(-player.runSpeed)
        if inputState.isSet('right'): speed.setX(player.runSpeed)
        if inputState.isSet('turnLeft'):  omega =  player.turnSpeed
        if inputState.isSet('turnRight'): omega = -player.turnSpeed
        if inputState.isSet('space'): self.doPlayerJump(player.bulletBody.node())
        if inputState.isSet('ctrl'): self.doPlayerCrouch(player)
        
        #player.bulletBody.node().setAngularMovement(omega)
        player.bulletBody.node().setLinearMovement(speed, True)
        
        
    def buildTriangleMesh(self, _obj, _levelEgg, _mass=0, _isDynamic=False):
        """Build a bullet TriangleMesh for objects"""
        
        mesh = BulletTriangleMesh()
        node = _obj.node()
        
        if node.isGeomNode():
            mesh.addGeom(node.getGeom(0))
        else:
            return
            
        body = BulletRigidBodyNode(_obj.getTag("level"))
        body.addShape(BulletTriangleMeshShape(mesh, dynamic=_isDynamic))
        body.setMass(_mass)
        
        np = self.engine.BulletObjects["level"].attachNewNode(body)
        np.setCollideMask(BitMask32.allOn())
        np.setScale(_obj.getScale(_levelEgg))
        np.setPos(_obj.getPos(_levelEgg))
        np.setHpr(_obj.getHpr(_levelEgg))
        
        self.engine.bulletWorld.attachRigidBody(body)
        
        return np
        
        
    def doRay(self, pfrom, target):
        
        pFrom = pfrom
        
        result = self.engine.bulletWorld.rayTestClosest(pFrom, target)
        
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
