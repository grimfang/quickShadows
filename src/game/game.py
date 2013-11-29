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

"""@ package Game

Start the Game.
"""

# System Imports
import logging as log

# Panda Engine Imports

# MeoTech Imports
from input import InputHandler

#----------------------------------------------------------------------#

# Game
class Game():
    """The Game handles the actual game and custom scripts.
    """
    def __init__(self, _meotech):
        
        print "Game - init >>>"
        
        # Meotech
        self.meotech = _meotech
        
        # Load Inputs
        self.inputs = InputHandler(self)
        
        # Add GameLoop Task
        taskMgr.add(self.gameLoop, "Game_loop")
        
        # Check the engine if we have a player.
        if self.meotech.engine.GameObjects["player"]:
            if self.meotech.engine.GameObjects["player"].useBasicMovement:
                self.hasPlayer = True

        else:
            self.hasPlayer = False


    def gameLoop(self, task):
        
        dt = globalClock.getDt()
        # Add player movement
        # Check this if its slow change it...
        if self.hasPlayer:
            #self.meotech.engine.factory.basePhysics.useBasicPlayerMovement(dt)
            self.inputs.getMouse(dt)
        # Add Player camera handler
        
        return task.cont
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
