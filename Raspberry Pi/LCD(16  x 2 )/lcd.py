import RPi.GPIO as GPIO 
import time
from RPLCD import CharLCD

# Configure the LCD
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

lcd.print("I am working")