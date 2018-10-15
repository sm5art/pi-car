import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
motor_pin = 26
GPIO.setup(motor_pin, GPIO.OUT)

try:
    GPIO.output(motor_pin, GPIO.HIGH)

    time.sleep(1)
    GPIO.output(motor_pin, GPIO.LOW)
finally:
    GPIO.cleanup()
