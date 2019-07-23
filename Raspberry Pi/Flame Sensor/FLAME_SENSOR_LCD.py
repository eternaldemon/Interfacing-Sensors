import RPi.GPIO as GPIO 
import time
from RPLCD import CharLCD

# Configure the LCD
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.OUT)
input = GPIO.input(3)
while True:
  if (GPIO.input(3)):
    lcd.write_string("Flame Detected")
    time.sleep(1)
    GPIO.output(5,True)
  else:
    lcd.write_string("Not Detected")
    delay(1)
    GPIO.output(5,False)
