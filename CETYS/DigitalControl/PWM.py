import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(12,gpio.OUT)

while True:
	freq = int(input('Valor del PWM:'))
	gpio.setmode(gpio.BOARD)
	gpio.setup(12,gpio.OUT)
	p = gpio.PWM(12,100)
	p.start(50)
	p.ChangeFrequency(freq)
	input('')
	p.stop()
	gpio.cleanup()


