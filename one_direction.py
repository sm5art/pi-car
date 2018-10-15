import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
forward_pin = 26
backward_pin = 19
GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(backward_pin, GPIO.IN)
n_seconds = 5

try:
    GPIO.output(forward_pin, GPIO.HIGH)
    time.sleep(5)
finally:
    GPIO.cleanup()


#while True:
    """command = raw_input().lower()
    if command == 'w':
        start = time.time()
        while(time.time() - start < n_seconds):
            GPIO.output(forward_pin, GPIO.HIGH)
            GPIO.output(backward_pin, GPIO.LOW)
    elif command == 's':
        start = time.time()
        while(time.time() - start < n_seconds):
            GPIO.output(forward_pin, GPIO.LOW)
            GPIO.output(backward_pin, GPIO.HIGH)
    else:
        start = time.time()
        while(time.time() - start < n_seconds):
            GPIO.output(forward_pin, GPIO.LOW)
            GPIO.output(backward_pin, GPIO.LOW)"""