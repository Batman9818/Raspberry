import RPi.GPIO AS GPIOimport time
pin=18
gpio.setmode(gpio.BCM)
gpio.setup(pin,gpio.OUT)
gpio.output(pin,True)
pwn=gpio.pwm(pin,500)
pwm.start()
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