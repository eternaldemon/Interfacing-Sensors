import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD 
from time import sleep

# Configure the LCD
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

#GPIO.setmode(GPIO.BCM)
Relay_channel = [38,40]
GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.LOW)

lcd.clear()
GPIO.output(Relay_channel[0], GPIO.HIGH)
lcd.write_string("Relay channel ")
lcd.write_string(str(1))
lcd.write_string(" is on ")
sleep(5)
GPIO.output(Relay_channel[0, GPIO.LOW)
lcd.write_string("Relay channel ")
lcd.write_string(str(1))
lcd.write_string(" is off ")
sleep(5)
GPIO.output(Relay_channel[1], GPIO.HIGH)
lcd.write_string("Relay channel ")
lcd.write_string(str(2))
lcd.write_string(" is on ")
sleep(5)
GPIO.output(Relay_channel[1], GPIO.LOW)
lcd.write_string("Relay channel ")
lcd.write_string(str(2))
lcd.write_string(" is off ")