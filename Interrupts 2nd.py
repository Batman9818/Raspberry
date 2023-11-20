import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Configure GPIO pins
pin_low_to_high = 17  # Pin for LOW to HIGH transition
pin_high_to_low = 18  # Pin for HIGH to LOW transition
led1 = 23  # LED for positive edge
led2 = 24  # LED for negative edge

# Set up GPIO pins
GPIO.setup(pin_low_to_high, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin_high_to_low, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

# Interrupt Service Routine for LOW to HIGH transition
def ISRL2H(pin):
    print("LOW to HIGH transition detected on Pin {}".format(pin))
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(1)  # LED1 on for 1 second
    GPIO.output(led1, GPIO.LOW)

# Interrupt Service Routine for HIGH to LOW transition
def ISRH2L(pin):
    print("HIGH to LOW transition detected on Pin {}".format(pin))
    GPIO.output(led2, GPIO.HIGH)
    time.sleep(1)  # LED2 on for 1 second
    GPIO.output(led2, GPIO.LOW)

try:
    while True:
        # Check for LOW to HIGH transition
        if GPIO.input(pin_low_to_high) == GPIO.HIGH:
            ISRL2H(pin_low_to_high)
            time.sleep(0.2)  # Debounce time

        # Check for HIGH to LOW transition
        if GPIO.input(pin_high_to_low) == GPIO.LOW:
            ISRH2L(pin_high_to_low)
            time.sleep(0.2)  # Debounce time

except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()