import RPi.GPIO as GPIO
import time 

buzzer_pin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)

def buzz(pitch,duration):
	period=1.0/pitch
	delay=period/2
	cycles=int(duration*pitch)
	for i in range(cycles):
		GPIO.output(buzzer_pin,True)
		time.sleep(delay)
		GPIO.output(buzzer_pin,False)
		time.sleep(delay)

while (True):
	pitch_s=input("Enter Pitch (200 to 2000): ")
	pitch=float(pitch_s)
	duration_s=input("Enter Duration (seconds): ")
	duration=float(duration_s)
	buzz(pitch,duration) 
