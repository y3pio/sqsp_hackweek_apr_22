import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

LASER_PIN_GREEN = 11
LASER_PIN_BLUE = 12

GPIO.setup(LASER_PIN_GREEN, GPIO.IN)
GPIO.setup(LASER_PIN_BLUE, GPIO.IN)

while True:
	print("GPIO: Green[%2d] - Blue[%2d]" % (GPIO.input(LASER_PIN_GREEN), GPIO.input(LASER_PIN_BLUE)))


print ('Hello World!')