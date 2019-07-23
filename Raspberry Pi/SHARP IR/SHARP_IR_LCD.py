import RPi.GPIO as GPIO 
import time
from RPLCD import CharLCD

# Configure the LCD
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

GPIO.setwarnings(False)
pin_no=3
#GPIO.setmode(GPIO.BCM)

GPIO.setup(5,GPIO.OUT)
GPIO.setup(pin_no,GPIO.IN) 

while 1:

    if(GPIO.input(pin_no)==True): 
        GPIO.output(5,False) 
        pulse_start = time.time()
    
    if(GPIO.input(pin_no)==False):
        GPIO.output(5,True)
        pulse_end = time.time()
        
pulse_duration=pulse_end-pulse_start

distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
distance = round(distance, 2)            #Round to two decimal points

if distance > 10 and distance < 80:      #Check whether the distance is within range
    #print("Distance:",distance,"cm" ) #Print distance with 0.5 cm calibration
    lcd.write_string(str(distance))
    time.sleep(0.5)
else:
    #print ("Out Of Range" )
    lcd.write_string("Out of Range")#display out of range
    time.sleep(0.5)

