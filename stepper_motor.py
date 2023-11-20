import RPi.GPIO as GPIO
import time

sequence = ['1010', '0110', '0101', '1001']
coil_A_1 = 2
coil_A_2 = 3
coil_B_1 = 4
coil_B_2 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(coil_A_1, GPIO.OUT)
GPIO.setup(coil_A_2, GPIO.OUT)
GPIO.setup(coil_B_1, GPIO.OUT)
GPIO.setup(coil_B_2, GPIO.OUT)
def forward(steps):
    for _ in range(steps):
        for step in sequence:
            set_step(step)
            time.sleep(1)
def reverse(steps):
    for _ in range(steps):
        for step in reversed(sequence):
            set_step(step)
            time.sleep(1)
def set_step(step):
    GPIO.output(coil_A_1, int(step[0]))
    GPIO.output(coil_A_2, int(step[1]))
    GPIO.output(coil_B_1, int(step[2]))
    GPIO.output(coil_B_2, int(step[3]))
try:
    while True:
        direction = input("Enter 'forward' or 'reverse' (q to quit): ")
        if direction == 'q':
            break
        steps = 2  
        if direction == 'forward':
            print("Moving forward...")
            forward(steps)
        elif direction == 'reverse':
            print("Moving reverse...")
            reverse(steps)
        else:
            print("Invalid input. Please enter 'forward' or 'reverse'.")

except KeyboardInterrupt:
    pass
GPIO.cleanup()
