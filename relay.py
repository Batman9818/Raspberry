import RPi.GPIO as GPIO
import time

relay=16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay,GPIO.OUT)
for i in range(4):
      GPIO.output(relay,GPIO.LOW)
      time.sleep(1)
      GPIO.output(relay,GPIO.HIGH)
      time.sleep(1)
GPIO.cleanup()

