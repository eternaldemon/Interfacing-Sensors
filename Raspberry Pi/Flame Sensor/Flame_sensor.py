import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.IN)
GPIO.setup(26,GPIO.OUT)
input = GPIO.input(2)
while True:
  if (GPIO.input(2)):
    print("Flame Detected")
    GPIO.output(26,True)
  else:
    print("Not Detected")
    GPIO.output(26,False)