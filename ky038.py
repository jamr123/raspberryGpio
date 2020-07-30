import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
flag=False
delay=0.05
print("inicio")
while True:
   if GPIO.input(4):
       time.sleep(180) 
       flag=not flag
       print(flag)
       GPIO.output(4,flag)
       GPIO.output(17,flag)

      
   