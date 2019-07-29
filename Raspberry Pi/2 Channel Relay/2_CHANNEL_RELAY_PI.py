import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM)
Relay_channel = [20,21]
GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(Relay_channel[0], GPIO.HIGH)
sleep(5)
GPIO.output(Relay_channel[0, GPIO.HIGH)
sleep(5)
GPIO.output(Relay_channel[1], GPIO.HIGH)
sleep(5)
GPIO.output(Relay_channel[1], GPIO.HIGH)
sleep(5)