import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
flag=False
delay=0.05
while True:
   if GPIO.input(3):
       time.sleep(180) 
       flag=not flag
       GPIO.output(4,flag)
       GPIO.output(17,flag)

      
   