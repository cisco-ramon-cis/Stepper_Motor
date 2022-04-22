from machine import Pin,
from time import sleep

#==== Pin numbers =====
_IN1 = Pin(0,Pin.OUT)
_IN2 = Pin(4,Pin.OUT)
_IN3 = Pin(27,Pin.OUT)
_IN4 = Pin(25,Pin.OUT)

#===========================
#===    Patterns  ====
#===========================

#== Full movemnts pattern ==
_full = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]]
#== Half movements pattern ==
_half = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]]
#== Whole movements pattern ==
_whole = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1]]

#+++++++++++++++++++++++++++++++++++++++++++++++++

#================  list-for-pins  ================
pins = [_IN1,_IN2,_IN3,_IN4]
#==== function to perform clockwise movements ====

def _clockwise(pattern):
    while True:
        for val in pattern:
            for j in range(len(pins)):
                pins[j].value(val[j])
                sleep(0.5)
            sleep(0.5)
        sleep(0.1)        
        
def _counterClockwise(pattern):
    while True:
        for val in pattern:
            Full.reverse()
            for j in range(len(pins)):
                pins[j].value(val[j])
                sleep(0.5)
            sleep(1)
#==================================================
            
'''
    ===============================================
    motion is either clockwise or counter clockwise
    ===============================================
    form is either 1 ,2 or 3
    1 = full
    2 = half
    3 = whole
    ===============================================
'''

#======== funciton to perform movements ===========
def move(motion,form):
    if motion == 1 and form == 1:
        _clockwise(_full)
    elif motion == 1 and form == 2:
        _clockwise(_half)
    elif motion == 1 and form == 3:
        _clockwise(_whole)
    elif motion == 2 and form == 1:
        _clockwise(_full)
    elif motion == 2 and form == 2:
        _clockwise(_half)
    elif motion == 2 and form == 3:
        _clockwise(_whole)