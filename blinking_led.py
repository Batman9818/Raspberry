import RPi.GPIO as GPIO
import time as time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)


def blink_led():
     while (True):
       GPIO.output(17,True)
       time.sleep(0.5)
       GPIO.output(17,False)
       time.sleep(0.5)
     


blink_led()
