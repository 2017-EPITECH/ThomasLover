import RPi.GPIO as GPIO
import time

LCD_RS = 21
LCD_E = 20
LCD_D4 = 12
LCD_D5 = 25
LCD_D6 = 24
LCD_D7 = 23

LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_byte(bits, mode):
	GPIO.output(LCD_RS, mode)

	GPIO.output(LCD_D4, False)
	GPIO.output(LCD_D5, False)
	GPIO.output(LCD_D6, False)
	GPIO.output(LCD_D7, False)

	if bits&0x10 == 0x10:
		GPIO.output(LCD_D4, True)
	if bits&0x20 == 0x20:
		GPIO.output(LCD_D5, True)
	if bits&0x40 == 0x40:
		GPIO.output(LCD_D6, True)
	if bits&0x80 == 0x80:
		GPIO.output(LCD_D7, True)

	lcd_toggle_enable()

	GPIO.output(LCD_D4, False)
	GPIO.output(LCD_D5, False)
	GPIO.output(LCD_D6, False)
	GPIO.output(LCD_D7, False)

	if bits&0x01 == 0x01:
		GPIO.output(LCD_D4, True)
	if bits&0x02 == 0x02:
		GPIO.output(LCD_D5, True)
	if bits&0x04 == 0x04:
		GPIO.output(LCD_D6, True)
	if bits&0x08 == 0x08:
		GPIO.output(LCD_D7, True)

	lcd_toggle_enable()

def lcd_init():
	GPIO.setwarnings(False)
	GPIO.setup(LCD_E, GPIO.OUT)
	GPIO.setup(LCD_RS, GPIO.OUT)
	GPIO.setup(LCD_D4, GPIO.OUT)
	GPIO.setup(LCD_D5, GPIO.OUT)
	GPIO.setup(LCD_D6, GPIO.OUT)
	GPIO.setup(LCD_D7, GPIO.OUT)

	lcd_byte(0x33, LCD_CMD)
	lcd_byte(0x32, LCD_CMD)
	lcd_byte(0x06, LCD_CMD)
	lcd_byte(0x0C, LCD_CMD)
	lcd_byte(0x28, LCD_CMD)
	lcd_byte(0x01, LCD_CMD)
	time.sleep(E_DELAY)


def lcd_toggle_enable():
	time.sleep(E_DELAY)
	GPIO.output(LCD_E, True)
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, False)
	time.sleep(E_DELAY)

def lcd_string(message, line):
	message = message.ljust(LCD_WIDTH, " ")

	lcd_byte(line, LCD_CMD)

	for i in range(LCD_WIDTH):
		lcd_byte(ord(message[i]), LCD_CHR)
