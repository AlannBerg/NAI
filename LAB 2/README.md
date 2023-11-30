 ## Adaptive Cruise Control Fuzzy Control System 
  Adaptive Cruise Control is present in almost every modern car, it's 
 job is to estimate safe distance to next car and adjust speed. This part of code
 will only estimate distance.
 
 ## Creators: Alan Berg, Tomasz Fidurski

## How to run :

    git clone https://github.com/AlannBerg/Nai-2-Adaptive-Cruise-Control-Fuzzy-Control-System-.git

    pip install scikit-fuzzy

    pip install matplotlib
    
 # This Adaptive Cruise Control will pay attention to 3 conditions:
  1) Car speed
 2) Temperature
 3) Car load

## Inputs
To input conditions edit 

    ''' Setting contitions '''
    distance_simulation.input['car_speed']= x from range(0-160)
    distance_simulation.input['temperature']= x from range (-50 , 50)
    distance_simulation.input['car_load']= x from range (0-100)


## Examples
