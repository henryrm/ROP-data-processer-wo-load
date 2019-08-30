# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:17:11 2019

@author: mhenry
"""


import numpy
import glob
import math
import os



def stressCalculator(data):
# declare lists
    ch0 = []
    ch1 = []
    ch2 = []
    allChannels = []

# put data into list 
    allChannels = data.split()

# delete header information
    del allChannels[0:49]

    allChannels = [float(i) for i in allChannels]


# iterate through list and save each channel to separate list 
    i2 = 0
    while i2 < len(allChannels):
        ch0.append(allChannels[i2])
        ch1.append(allChannels[i2+1])
        ch2.append(allChannels[i2+2])
        i2 = i2+3
    
# for each channel, find the break point 
    
# define break point variables    
    ch0BreakPoint = 0
    ch1BreakPoint = 0
    ch2BreakPoint = 0

# define iterator variables
    i3 = 0
    i4 = 0
    i5 = 0

# loops through the channel taking the absolute difference between consecutive points
# if the difference > 10 then it is saved as the break point
    while i3 < len(ch0):
        if abs(ch0[i3+1]-ch0[i3]) < 10:
            i3 = i3+1
            else:
                ch0BreakPoint = ch0[i3]
                break
    
    while i4 < len(ch1):
        if abs(ch1[i4+1]-ch1[i4]) < 10:
            i4 = i4+1
            else:
                ch1BreakPoint = ch1[i4]
                break       
        
        while i5 < len(ch2):
            if abs(ch2[i5+1]-ch2[i5]) < 10:
                i5 = i5+1
                else:
                    ch2BreakPoint = ch2[i5]
                    break      
        
# calculate stress values using rosette strain equation  
    maxStrain = 0
    minStrain = 0
    stress = 0
    v = 0.23
    E = 71.54

    maxStrain = 0.5*((ch0BreakPoint+ch2BreakPoint)+math.sqrt((2*(ch0BreakPoint-ch1BreakPoint)**2)+(2*(ch2BreakPoint-ch1BreakPoint)**2)))
    minStrain = 0.5*((ch0BreakPoint+ch2BreakPoint)-math.sqrt((2*(ch0BreakPoint-ch1BreakPoint)**2)+(2*(ch2BreakPoint-ch1BreakPoint)**2)))

# round values to 2 decimal places (this is how our template works)
    maxStrain = round(maxStrain,2)
    minStrain = round(minStrain,2)
       
    stress = ((E/(1-v**2))*(maxStrain+v*minStrain))/1000
    stress = round(stress,2)
    
    print("Stress (MPa) = ", stress) 