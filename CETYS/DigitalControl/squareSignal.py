#from scipy import signal
import numpy as np
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(12,gpio.OUT)
while True:
	gpio.cleanup()
	gpio.setmode(gpio.BOARD)
	gpio.setup(12,gpio.OUT)
	gpio.setwarnings(False)

	p = gpio.PWM(12,1)
	p.start(10)
	time.sleep(10)
	#raw_input('')
#	gpio.cleanup()
#	time.sleep(10)
