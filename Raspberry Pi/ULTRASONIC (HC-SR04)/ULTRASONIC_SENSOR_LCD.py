import RPi.GPIO as GPIO 
import time
from RPLCD import CharLCD

# Configure the LCD
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

#GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

TRIG = 16                                  #Associate pin 23 to TRIG
ECHO = 18                                  #Associate pin 24 to ECHO

print ("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

try:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print ("Waitng For Sensor To Settle")
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  pulse_start=0
  pulse_end=0
  echo_state =0
  

  while echo_state==0:                       #Check whether the ECHO is LOW
      echo_state=GPIO.input(ECHO)
      pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:                 #Check whether the ECHO is HIGH
        pulse_end = time.time()              #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start   #Get pulse duration to a variable

  distance = pulse_duration * 17150          #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)              #Round to two decimal points

  if distance > 2 and distance < 400:        #Check whether the distance is within range
    #print ("Distance:",distance,"cm" )      #Print distance with 0.5 cm calibration
    lcd.write_string(str(distance))
    time.sleep(1)

  else:
    lcd.write_string("Out Of Range" )
    time.sleep(1)
