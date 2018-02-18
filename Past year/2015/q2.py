# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:17:58 2017

@author: Kenny

state
desired distance to actial distance
sensed distance to the wall "dsensed:".
Controller
k(dDesired-dSensed)

k  should be a negative number( When dDesired >dSensed we want to reduce the distance)
"""
import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
dDesired = 0.7
k = -5# Please suggest a value of k
# Input is output of Sensor machine (below); output is an action.
# Note that this machine must also compute E, the error, and output
# the velocity, based on that.
class Controller(sm.SM):
    def getNextValues(self, state, inp):
        fvel = k * (dDesired - inp)
        rvel = 0
        return state, io.Action(fvel, rvel)
# Input is SensorInput instance;
# output is a delayed front sonar reading
class Sensor(sm.SM):
    def __init__(self, initDist, numDelays):
        self.startState = [initDist]*numDelays
    def getNextValues(self, state, inp):
        print inp.sonars[3]
        output = state[-1]
        state = [inp.sonars[3]] + state[:-1]
        return (state, output)
mySM = sm.Cascade(Sensor(1.5, 1), Controller())
mySM.name = 'brainSM'



