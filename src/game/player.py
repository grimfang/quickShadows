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

"""@ package Player

Setup player and related
"""

# System Imports
import logging as log

# Panda Engine Imports
from panda3d.core import Spotlight, VBase4, PerspectiveLens

# MeoTech Imports

#----------------------------------------------------------------------#

class Player():

    def __init__(self, _base):
        self.game = _base

        # Player object
        self.playerObject = self.game.meotech.engine.GameObjects["player"]

        # Attach the flashlight cone to the player (self, _height, _radius, _pos, _hpr)
        self.flashlightConeBody = self.game.meotech.engine.factory.basePhysics.buildConeShape(10.0, 1.5,
                                                                                              self.playerObject.bulletBody.getPos(), self.playerObject.bulletBody.getHpr())

        # Attach the flashlight model to the player
        self.flashlight = loader.loadModel("game/models/flashlight")
        self.flashlight.setScale(0.2)
        self.flashlight.reparentTo(self.flashlightConeBody)

        # Attach the light to the flashlight model
        slight = Spotlight('slight')
        slight.setColor(VBase4(1, 1, 1, 1))
        lens = PerspectiveLens()
        lens.setFar(25)
        lens.setFov(40, 40)
        slight.setLens(lens)
        slight.setShadowCaster(True, 512, 512)
        self.flashlightLight = render.attachNewNode(slight)
        self.flashlightLight.reparentTo(self.flashlight.find("LightPos"))
        render.setLight(self.flashlightLight)

        self.flashlightConeBody.reparentTo(self.playerObject.bulletBody)
        self.flashlightConeBody.setPos(base.cam.getPos())

        #base.oobe()
