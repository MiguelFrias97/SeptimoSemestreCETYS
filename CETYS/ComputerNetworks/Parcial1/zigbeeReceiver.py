import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=3)
print('connecting Serial Port')

while True:
#	print ('Waiting...')
	line = ser.readline().strip()
	print(line)
