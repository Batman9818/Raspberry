import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5,GPIO.OUT)
try:
  while True:
         i=GPIO.input(12)
         if i==1:
             print("MOTION DETECTED",i)
             GPIO.output(5,1)
             time.sleep(0.1)
         else:
             print("no MOTION DETECTED",i)
             GPIO.output(5,0)
except KeyboardInterrupt:
         GPIO.cleanup()
