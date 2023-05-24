# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 06:26:45 2019

battery_power:Total energy a battery can store in one time measured in mAh
blue:Has bluetooth or not
clock_speed:speed at which microprocessor executes instructions
dual_sim:Has dual sim support or not
fc:Front Camera mega pixels
four_g:Has 4G or not
int_memory:Internal Memory in Gigabytes
m_dep:Mobile Depth in cm
mobile_wt:Weight of mobile phone
n_cores:Number of cores of processor
pc:Primary Camera mega pixels
px_height:Pixel Resolution Height
px_width:Pixel Resolution Width
ram:Random Access Memory in Mega Bytes
sc_h:Screen Height of mobile in cm
sc_w:Screen Width of mobile in cm
talk_time:longest time that a single battery charge will last when you are
three_g:Has 3G or not
touch_screen:Has touch screen or not
wifi:Has wifi or not
price_range:This is the target variable with value of 0(low cost), 1(medium cost), 2(high cost) and 3(very high cost)

@author: Rajeev Ranjan Pandey
"""
import pandas as pd
mydata_train=pd.read_csv(r"train.csv")
X_input = mydata_train.drop(['price_range'],axis=1)
Y_output = mydata_train['price_range']
from sklearn.neighbors import KNeighborsClassifier
myobj = KNeighborsClassifier()
mymodel = myobj.fit(X_input,Y_output)
'''
mydata_test=pd.read_csv(r"test.csv")
X_test = mydata_test.drop(['id'],axis=1)
print(mymodel.predict(X_test))
'''
print("Enter values of the following attributes for the new phone:")
battery_power = input("Enter Total energy its battery can store in one time measured in mAh: ")
blue = input("Enter if it Has bluetooth or not <1/0>: ")
clock_speed = input("Enter speed at which microprocessor executes instructions: ")
dual_sim = input("Enter if it Has dual sim support or not <1/0>: ")
fc = input("Enter Front Camera mega pixels: ")
four_g = input("Enter if it Has 4G or not <1/0>: ")
int_memory = input("Enter Internal Memory in Gigabytes: ")
m_dep = input("Enter Mobile Depth in cm: ")
mobile_wt = input("Enter Weight of mobile phone: ")
n_cores = input("Enter Number of cores of processor: ")
pc = input("Enter Primary Camera mega pixels: ")
px_height = input("Enter Pixel Resolution Height: ")
px_width = input("Enter Pixel Resolution Width: ")
ram = input("Enter Random Access Memory in Mega Bytes: ")
sc_h = input("Enter Screen Height of mobile in cm: ")
sc_w = input("Enter Screen Width of mobile in cm: ")
talk_time = input("Enter longest time that a single battery charge will last: ")
three_g = input("Enter if it Has 3G or not <1/0>: ")
touch_screen = input("Enter if it Has touch screen or not <1/0>: ")
wifi = input("Enter if it Has wifi or not <1/0>: ")
new_mobile = [battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi]
priceRange = mymodel.predict([new_mobile])
if priceRange==0:
    print("The new phone is of low cost")
elif priceRange==1:
    print("The new phone is of medium cost")
elif priceRange==2:
    print("The new phone is of high cost")
elif priceRange==3:
    print("The new phone is of very high cost")
