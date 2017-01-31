import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.setup(5, GPIO.OUT)
while True:
    if(GPIO.input(6) == 1):
        GPIO.output(5,1)
        time.sleep(5)

