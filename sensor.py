import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import firebase_io

GPIO.setmode(GPIO.BOARD)

LASER_PIN_GREEN = 11
LASER_PIN_BLUE = 12

GREEN_TIME = None
BLUE_TIME = None

GPIO.setup(LASER_PIN_GREEN, GPIO.IN)
GPIO.setup(LASER_PIN_BLUE, GPIO.IN)

PIN_IN_DEBOUNCE = 1

GPIO.add_event_detect(LASER_PIN_GREEN, GPIO.FALLING, bouncetime=PIN_IN_DEBOUNCE)
GPIO.add_event_detect(LASER_PIN_BLUE, GPIO.FALLING, bouncetime=PIN_IN_DEBOUNCE)

customer_count = 0

try:
	while True:
		# print("%s - %s | Count: %2d" % (GREEN_TIME, BLUE_TIME, customer_count))

		if GPIO.event_detected(LASER_PIN_GREEN):
			print("Trip Alert: GREEN - %s" % datetime.now())
			GREEN_TIME = datetime.now()

		if GPIO.event_detected(LASER_PIN_BLUE):
			print("Trip Alert: BLUE - %s" % datetime.now())
			BLUE_TIME = datetime.now()

		if (GREEN_TIME and BLUE_TIME):
			GPIO.remove_event_detect(LASER_PIN_GREEN)
			GPIO.remove_event_detect(LASER_PIN_BLUE)

			print("%s - %s | Current count: %2d" % (GREEN_TIME, BLUE_TIME, customer_count))
			if (GREEN_TIME < BLUE_TIME):
				print("Customer +1 IN")
				customer_count+=1
				firebase_io.update_firebase(1)
			else:
				print("Customer -1 OUT")
				customer_count-=1
				firebase_io.update_firebase(-1)

			sleep(1.75)

			GREEN_TIME = None
			BLUE_TIME = None

			print("Resetting timer (should be None): %s - %s | Current count: %2d" % (GREEN_TIME, BLUE_TIME, customer_count))

			GPIO.add_event_detect(LASER_PIN_GREEN, GPIO.FALLING, bouncetime=PIN_IN_DEBOUNCE)
			GPIO.add_event_detect(LASER_PIN_BLUE, GPIO.FALLING, bouncetime=PIN_IN_DEBOUNCE)

			

		# sleep(.3)
except KeyboardInterrupt:
    pass

print("Total customer count: ", customer_count)

GPIO.cleanup()
print ('Hello World!')