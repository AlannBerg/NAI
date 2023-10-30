import dis
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
 Adaptive Cruise Control Fuzzy Control System 

 Creators: Alan Berg, Tomasz Fidurski

To run program install
pip install scikit-fuzzy
pip install matplotlib

 Adaptive Cruise Control is present in almost every modern car, it's 
 job is to estimate safe distance to next car and adjust speed. This part of code
 will only estimate distance.

 This Adaptive Cruise Control will pay attention to 3 conditions:
 1) Car speed
 2) Temperature
 3) Car load

 Car speed - as car speed increase the distance between cars should also increase, because 
             breaking distance will also increase

Temperature - when it's cold outside tires have less grip, breaking distance will increase

Car load - when car have to break with extra weight it will increase breaking distance

'''
# Car speed in km per hour
car_speed = ctrl.Antecedent(np.arange(0, 160, 1), 'car_speed')
# Temperature in celsius degrees
temperature = ctrl.Antecedent(np.arange(-50, 50, 1), 'temperature')
# Car load in percents, 100 means 100% of max car load.
car_load = ctrl.Antecedent(np.arange(0, 100, 1), 'car_load')
# Safe distance between cars in meters
safe_distance = ctrl.Consequent(np.arange(0, 200, 1), 'safe_distance')

car_speed['low'] = fuzz.trimf(car_speed.universe, [0, 0, 50])
car_speed['average'] = fuzz.trimf(car_speed.universe, [40, 85, 100])
car_speed['high'] = fuzz.trimf(car_speed.universe, [80, 160, 160])

temperature['low'] = fuzz.trimf(temperature.universe, [-50, -50, 10])
temperature['average'] = fuzz.trimf(temperature.universe, [5, 10, 15])
temperature['high'] = fuzz.trimf(temperature.universe, [15, 50, 50])

car_load['low'] = fuzz.trimf(car_load.universe, [0, 0, 35])
car_load['average'] = fuzz.trimf(car_load.universe, [30, 40, 60])
car_load['high'] = fuzz.trimf(car_load.universe, [50, 100, 100])

safe_distance['low'] = fuzz.trimf(safe_distance.universe, [0, 0, 35])
safe_distance['average'] = fuzz.trimf(safe_distance.universe, [30, 60, 100])
safe_distance['high'] = fuzz.trimf(safe_distance.universe, [80, 200, 200])


car_speed['average'].view()
temperature['average'].view()
car_load['average'].view()
safe_distance['average'].view()

'''
Specifing rules, when there is cold outside, or car load is high, distance should be increaced
'''

''' When car speed is low '''
rule1=ctrl.Rule(car_speed['low']&temperature['low']&car_load['low'], safe_distance['low'])
rule2=ctrl.Rule(car_speed['low']&temperature['low']&car_load['average'], safe_distance['average'])
rule3=ctrl.Rule(car_speed['low']&temperature['low']&car_load['high'], safe_distance['average'])
rule4=ctrl.Rule(car_speed['low']&temperature['average']&car_load['low'], safe_distance['low'])
rule5=ctrl.Rule(car_speed['low']&temperature['average']&car_load['average'], safe_distance['low'])
rule6=ctrl.Rule(car_speed['low']&temperature['average']&car_load['high'], safe_distance['average'])
rule7=ctrl.Rule(car_speed['low']&temperature['high']&car_load['low'], safe_distance['low'])
rule8=ctrl.Rule(car_speed['low']&temperature['high']&car_load['average'], safe_distance['low'])
rule9=ctrl.Rule(car_speed['low']&temperature['high']&car_load['high'], safe_distance['average'])
''' When car speed is average '''
rule10=ctrl.Rule(car_speed['average']&temperature['low']&car_load['low'], safe_distance['average'])
rule11=ctrl.Rule(car_speed['average']&temperature['low']&car_load['average'], safe_distance['average'])
rule12=ctrl.Rule(car_speed['average']&temperature['low']&car_load['high'], safe_distance['high'])
rule13=ctrl.Rule(car_speed['average']&temperature['average']&car_load['low'], safe_distance['average'])
rule14=ctrl.Rule(car_speed['average']&temperature['average']&car_load['average'], safe_distance['average'])
rule15=ctrl.Rule(car_speed['average']&temperature['average']&car_load['high'], safe_distance['average'])
rule16=ctrl.Rule(car_speed['average']&temperature['high']&car_load['low'], safe_distance['low'])
rule17=ctrl.Rule(car_speed['average']&temperature['high']&car_load['average'], safe_distance['average'])
rule18=ctrl.Rule(car_speed['average']&temperature['high']&car_load['high'], safe_distance['average'])
''' When car speed is high '''
rule19=ctrl.Rule(car_speed['high']&temperature['low']&car_load['low'], safe_distance['average'])
rule20=ctrl.Rule(car_speed['high']&temperature['low']&car_load['average'], safe_distance['high'])
rule21=ctrl.Rule(car_speed['high']&temperature['low']&car_load['high'], safe_distance['high'])
rule22=ctrl.Rule(car_speed['high']&temperature['average']&car_load['low'], safe_distance['average'])
rule23=ctrl.Rule(car_speed['high']&temperature['average']&car_load['average'], safe_distance['average'])
rule24=ctrl.Rule(car_speed['high']&temperature['average']&car_load['high'], safe_distance['high'])
rule25=ctrl.Rule(car_speed['high']&temperature['high']&car_load['low'], safe_distance['average'])
rule26=ctrl.Rule(car_speed['high']&temperature['high']&car_load['average'], safe_distance['average'])
rule27=ctrl.Rule(car_speed['high']&temperature['high']&car_load['high'], safe_distance['high'])

''' Creating control system '''
distance_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
''' Creating control simulation '''
distance_simulation = ctrl.ControlSystemSimulation(distance_ctrl)
''' Setting contitions '''
distance_simulation.input['car_speed']=20
distance_simulation.input['temperature']=10
distance_simulation.input['car_load']=50
''' Computing simulation '''
distance_simulation.compute()

''' Pringing out conditions '''
print ('Conditions : \n car speed {} km/h \n temperature: {} C \n car max load {} %'.format(
       distance_simulation._get_inputs()['car_speed'],
       distance_simulation._get_inputs()['temperature'],
       distance_simulation._get_inputs()['car_load']))

safe_distance_for_conditions = round(distance_simulation.output['safe_distance'])

print ("Safe distance {} m".format(safe_distance_for_conditions))

safe_distance.view(sim=distance_simulation)

plt.show() 