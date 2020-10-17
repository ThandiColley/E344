import numpy as np
from statistics import mean

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################
    # temperature = 0

    Vout_mean = mean(amplitude[len(amplitude) - 20:len(amplitude]))
    temperature = Vout_mean*2.014 + 32.916
        
        
    ######################################
        
    return temperature
        
