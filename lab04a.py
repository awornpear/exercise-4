# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:34:40 2020

@author: Benny
"""


data_file = open('data.txt', 'r')
totalh= 0
numlines= 0
totalw= 0
minheight= 1000.0
minweight= 1000.0
height = 0
weight = 0
maxheight = 0
maxweight = 0
bmi = 'BMI'
bmi_min = 1000
bmi_max= 0
bmi_str = 'BMI'

for line in data_file:
    line=line.strip()
    height= line[12:18].strip()
    weight= line[24:].strip()
    #if height.isalpha() == True:
        #print(line)
    if height.isalpha()!= True:
        totalh= totalh + float(height)
        totalw= totalw + float(weight)
        numlines +=1
        if float(height) < float(minheight):
            minheight = height
            
        if float(weight) < float(minweight):
            minweight = weight
            
        if float(height) > float(maxheight):
            maxheight= height
            
        if float(weight) > float(maxweight):
            maxweight = weight
            
        bmi= float(weight)/float(height) **2
        bmi_str = str(bmi)
        if bmi < bmi_min:
            bmi_min= bmi
        if bmi > bmi_max:
            bmi_max = bmi
    print('{:<37s}{:<13.5s}'.format(line,bmi_str))
        
      
        
            
            
averageh = totalh / numlines

averagew = totalw / numlines

averagebmi = averagew/ averageh **2



print("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",averageh, averagew, averagebmi))
print("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",float(maxheight), float(maxweight), bmi_max))
print('\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}'.format('Min', float(minheight), float(minweight), bmi_min))       
    
data_file.close()



