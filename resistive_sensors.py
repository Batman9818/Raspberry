import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
a=11
b=15
def discharge():
    GPIO.setup(a,GPIO.IN)
    GPIO.setup(b,GPIO.OUT)
    GPIO.output(b,False)
    time.sleep(0.005)
def charge():
    GPIO.setup(b,GPIO.IN)
    GPIO.setup(a,GPIO.OUT)
    c=0
    GPIO.output(a,True)
    while not GPIO.input(b):
        c=c+1
    return c
def analog():
    discharge()
    return charge()

while True:
      print(analog())
      time.sleep(1)
