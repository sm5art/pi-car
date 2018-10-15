import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
motor_pin = 26
GPIO.setup(motor_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(motor_pin, GPIO.HIGH)
finally:
    GPIO.cleanup()
