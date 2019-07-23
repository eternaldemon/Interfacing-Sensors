import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

sensor_pin = 2
led_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(sensor_pin,GPIO.IN)

current_state = 0

while True:
    time.sleep(0.1)
    current_state = GPIO.input(sensor_pin)
    if current_state == 0:
        print("Collision occured")
        GPIO.output(led_pin,True)
    else:
        print("No collision")
        GPIO.output(led_pin,False)
            
GPIO.cleanup()
