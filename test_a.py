import Jetson.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
out_a = 13

GPIO.setup(out_a, GPIO.OUT, initial=GPIO.LOW)
while(True):

	GPIO.output(out_a, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(out_a, GPIO.LOW)
	time.sleep(1)
GPIO.cleanup()
