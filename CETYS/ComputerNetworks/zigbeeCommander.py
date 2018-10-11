import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
print ('Connecting Serial Port')

while True:
	ser.write(b'Hello!\n')
	print('Saying: Hello!')
	time.sleep(1)
