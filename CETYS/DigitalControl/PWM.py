import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(12,gpio.OUT)
gpio.setwarnings(False)

while True:
	gpio.setmode(gpio.BOARD)
	gpio.setup(12,gpio.OUT)
	p = gpio.PWM(12,1)
	p.start(10)
	time.sleep(2)
	p.stop()
	gpio.cleanup()
	time.sleep(5)


