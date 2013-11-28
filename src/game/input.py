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
"""@ package Input

Keep all inputs here.
"""

# System imports
import logging as log
import sys

# Panda imports
from direct.showbase.InputStateGlobal import inputState

# MeoTech imports


#----------------------------------------------------------------------#

class InputHandler():
    """InputHandler.
    Keyboard stuff
    """
    def __init__(self, _game):
        """InputHandler INIT"""
        
        # Game
        self.game = _game
        
        # Keyboard
        inputState.watchWithModifiers('forward', 'w')
        inputState.watchWithModifiers('left', 'a')
        inputState.watchWithModifiers('reverse', 's')
        inputState.watchWithModifiers('right', 'd')
        inputState.watchWithModifiers('turnLeft', 'q')
        inputState.watchWithModifiers('turnRight', 'e')
        inputState.watchWithModifiers('space', 'space')
        #inputState.watchWithModifiers('ctrl', 'lcontrol_down')
        
        # App exit temp
        base.accept("escape", sys.exit)
        
        # mouse
        self.winXhalf = base.win.getXSize()/2
        self.winYhalf = base.win.getYSize()/2
        
        # Should move the camera stuff to the baseCamera.py
        base.camera.reparentTo(self.game.meotech.engine.GameObjects["player"].bulletBody)
        base.camLens.setFov(90)
        base.camLens.setNear(0.5)
        
        
        self.mouseSpeedX = 5
        self.mouseSpeedY = 0.2
        self.camP = 10
        
        
    def getMouse(self, dt):
        
        # Handle mouse
        md = base.win.getPointer(0)
        x = md.getX()
        y = md.getY()
        
        if base.win.movePointer(0, self.winXhalf, self.winYhalf):
            omega = (x - self.winXhalf)*-self.mouseSpeedX
            self.game.meotech.engine.GameObjects["player"].bulletBody.node().setAngularMovement(omega)
            cam = base.cam.getP() - (y - self.winYhalf) * self.mouseSpeedY
            if cam <-80:
                cam = -80
            elif cam > 90:
                cam = 90
            base.cam.setP(cam)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
