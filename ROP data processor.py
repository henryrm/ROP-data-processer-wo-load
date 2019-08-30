# -*- coding: utf-8 -*-
"""
Spyder Editor

# name: ring on ring/point data processor
# author: maggie h
# date: 5/16/2019
# version: 1.2 5.22.2019
# purpose: to expedite the data processing of ring on ring/ring on point testing
# current issues: this can handle all txt files in a directory
#                 can delete header no matter what samples are named 
#                 need to be able to output data to file
#                 
"""

import math
import os



#path = 'c:\users\mhenry\documents\201903077 python test'

# prompt user for file path 
print("Enter the file path: ")
path = input()

# save file names into list
fileList = os.listdir(path)
fileName = 0

##########################################
def removeIthWord(lst,word,N):
    count = 0
    indexCh = 0
  
    # iterate the elements 
    for i in range(len(lst)):
       # while count != N:
            if(lst[i] == word): 
                count = count + 1
                i = i+1
                if(count == N):
                    indexCh = i
                    break
#    print(indexCh)        
    if count == 0: 
        print("Item not found")     
      
    return indexCh
###############################################

###############################################
def stressCalculator(data):

# read the contents of file into string var data
    data = data.read()

# declare lists
    ch0 = []
    ch1 = []
    ch2 = []
    allChannels = []
    indexCh = 0

# put data into list 
    allChannels = data.split()

# delete header information
# loop through header info, find 3rd occurance of "Ch", then find index of start of Ch0
    indexCh = removeIthWord(allChannels,"Ch",3)
    del allChannels[0:indexCh+1]
         
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
        if abs(ch0[i3+1]-ch0[i3]) < 20:
            i3 = i3+1
        else:
            ch0BreakPoint = ch0[i3]
            break
    
    while i4 < len(ch1):
        if abs(ch1[i4+1]-ch1[i4]) < 20:
            i4 = i4+1
        else:
            ch1BreakPoint = ch1[i4]
            break       
        
        while i5 < len(ch2):
            if abs(ch2[i5+1]-ch2[i5]) < 20:
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

#################################################################
    
    
for fileName in fileList:
    if fileName.endswith(".txt"):
        f = open(fileName)
        stressCalculator(f)
        continue
    else:
        continue
            
    
    

    








