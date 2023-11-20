import RPi.GPIO as GPIO
import time

low_to_high_pin=17
high_to_low_pin=18

GPIO.setmode(GPIO.BCM)

GPIO.setup(low_to_high_pin,GPIO.IN)
GPIO.setup(high_to_low_pin,GPIO.IN)

def low_to_high_callback(channel):
      print("LOW to HIGH transition detected on GPIO",channel)
def high_to_low_callback(channel):
      print("HIGH to LOW transition detected on GPIO",channel)

GPIO.add_event_Detect(low_to_high_pin, GPIO.RISING,callback=low_to_high_callback, bouncetime=200)

GPIO.add_event_Detect(high_to_low_pin, GPIO.FALLING,callback=high_to_low_callback, bouncetime=200)

try:
  print("Waiting for interrupts. Press Ctrl+C to exit.")
  while True:
       time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
