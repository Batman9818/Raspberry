import RPi.GPIO AS gpio
import time
pin=18
gpio.setmode(gpio.BCM)
gpio.setup(pin,gpio.OUT)
gpio.output(pin,True)
pwm=gpio.PWM(pin,500)
pwm.start(100)
try:
    while True:
        gpio.output(pin,True)
        time.sleep(1)
        duty=int(input("Enter Duty Cycle:"))
        if duty<0 and duty>100:
            print("CYCLE VALUE SHOULD BE AROUND 1 TO 100")
            continue
        gpio.output(pin,False)
        time.sleep(1)
        pwm.ChangeDutyCycle(duty)
except KeyboardInterrupt:
    gpio.cleanup()
