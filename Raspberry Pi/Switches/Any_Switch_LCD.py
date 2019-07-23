import RPi.GPIO as GPIO 
import time
from RPLCD import CharLCD

# Configure the LCD
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

sensor_pin = 3
led_pin = 37

#GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(sensor_pin,GPIO.IN)

current_state = 0

while True:
    time.sleep(0.1)
    current_state = GPIO.input(sensor_pin)
    if current_state == 0:
        lcd.write_string("Collision occured")
        time.sleep(1)
        GPIO.output(led_pin,True)
    else:
        lcd.write_string("No collision")
        time.sleep(1)
        GPIO.output(led_pin,False)
            
GPIO.cleanup()

