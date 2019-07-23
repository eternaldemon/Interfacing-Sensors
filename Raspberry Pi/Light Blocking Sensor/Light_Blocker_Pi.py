#!/usr/bin/env python
import RPi.GPIO as GPIO
OutLed = 20 
LightInPin = 21
GPIO.setwarnings(False)
 
def setup():
    GPIO.setmode(GPIO.BCM) # Set GPIO as PIN Numbers 
    GPIO.setup(OutLed, GPIO.OUT) # Set Green Led Pin mode to output
    GPIO.setup(LightInPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pull up to high level(3.3V)
    GPIO.add_event_detect(LightInPin, GPIO.BOTH, callback=detect, bouncetime=200)
 
def Led(x):
    if x == 0:
        GPIO.output(OutLed, 1)
    if x == 1:
        GPIO.output(OutLed, 0)
 
def Print(x):
    if x == 1:
        print (' 14CORE | Light Interrupter')
        print (' --------------------------')
        print (' Light has been interrupted')
        print (' --------------------------')
 
def detect(chn):
    Led(GPIO.input(LightInPin))
    Print(GPIO.input(LightInPin))
 
def loop():
    while True:
        pass
 
def destroy():
    GPIO.output(OutLed, GPIO.HIGH) # Green led off
    GPIO.output(Rpin, GPIO.HIGH) # Red led off
    GPIO.cleanup() # Release resource
 
if __name__ == '__main__': # Set the Program start from here
    setup()
try:
    loop()
except KeyboardInterrupt: # When pressed 'Ctrl+C' child program destroy() will be executed.
    destroy()