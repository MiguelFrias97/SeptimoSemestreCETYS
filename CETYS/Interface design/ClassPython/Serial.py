import serial

port = serial.Serial("/dev/ttyS0", baudrate = 115200, timeout = 3.0)

while True:
	port.write("\r\nSay Something:")
	rcv = port.read(10)
	port.write("\r\n You sent: " + repr(rcv))

