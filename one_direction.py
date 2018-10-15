import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
forward_pin = 26
backward_pin = 19
GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(backward_pin, GPIO.OUT)

try:
    while True:
        command = input().lower()
        if command == 'w':
            GPIO.output(forward_pin, GPIO.HIGH)
            GPIO.output(backward_pin, GPIO.LOW)
        elif command == 's':
            GPIO.output(forward_pin, GPIO.LOW)
            GPIO.output(backward_pin, GPIO.HIGH)
        else:
            GPIO.output(forward_pin, GPIO.LOW)
            GPIO.output(backward_pin, GPIO.LOW)
finally:
    GPIO.cleanup()
