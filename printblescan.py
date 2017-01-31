import blescan
import sys
import LCD as lcd
import RPi.GPIO as GPIO
from time import sleep

import bluetooth._bluetooth as bluez

servo = 18
button = 19
led = 5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

servo_motor = GPIO.PWM(servo, 50)
servo_motor.start(0)

left_angle = 12.5
center_angle = 7.5
right_angle = 2.5

def servo_mortor_control():

    try:
        if(GPIO.input(button)==0):
            servo_motor.ChangeDutyCycle(right_angle)
            print("Button Pressed")
            lcd.lcd_string("Door is open", lcd.LCD_LINE_1)
            GPIO.output(led, 1)
            sleep(5)
            servo_motor.ChangeDutyCycle(left_angle)
            sleep(0.5)
            print("Button Released")
            lcd.lcd_string("Door is closed", lcd.LCD_LINE_1)
            GPIO.output(led, 0)
            sleep(0.5)

    except KeyboardInterrupt:
        servo_motor.stop()
        GPIO.cleanup()

dev_id = 0
try:
        lcd.lcd_init()
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10) 
        len_returnedList = len(returnedList)

        if(len_returnedList > 0):
            servo_mortor_control()

	print "----------"
	for beacon in returnedList:
		print beacon
        lcd.lcd_string("", lcd.LCD_LINE_1)
        sleep(1)

