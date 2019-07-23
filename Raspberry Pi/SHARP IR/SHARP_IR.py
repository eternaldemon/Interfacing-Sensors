import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
pin_no=2
GPIO.setmode(GPIO.BCM)

GPIO.setup(26,GPIO.OUT)
GPIO.setup(2,GPIO.IN) 

while 1:

    if(GPIO.input(2)==True): 
        GPIO.output(26,False) 
        pulse_start = time.time()
    
    if(GPIO.input(2)==False):
        GPIO.output(26,True)
        pulse_end = time.time()
        
pulse_duration=pulse_end-pulse_start

distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
distance = round(distance, 2)            #Round to two decimal points

if distance > 10 and distance < 80:      #Check whether the distance is within range
    print ("Distance:",distance,"cm" ) #Print distance with 0.5 cm calibration
else:
    print ("Out Of Range" )                  #display out of range


