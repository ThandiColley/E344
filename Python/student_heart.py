import numpy as np

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################

    beat = 0
    i = 0
    
    nowA = 0
    preA = 0

    startT = 0
    endT = 0

    for time in np.arange(0, 6, 0.001):
        nowA = amplitude[i]

        if nowA > (preA + 4):
            if beat == 0:
                startT = time

            beat += 1
            endT = time

        preA = amp
        i += 1

    bpm = round(((beat - 1)/(endT - startT))*60)
        
    ######################################
        
    return bpm
        
