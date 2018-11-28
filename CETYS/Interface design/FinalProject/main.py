from threading import *

import json
import time
import socket
import sys
import RPi.GPIO as gpio


controlJson = '{}'
lock = Lock()

def socketCommunication():
	global controlJson
# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
	server_address = ('', 9000)
#	print('starting up on {} port {}'.format(*server_address))
	sock.bind(server_address)

    # Listen for incoming connections
	sock.listen(1)

	while True:
        # Wait for a connection
#		print('waiting for a connection')
		connection, client_address = sock.accept()
		try:
#			print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
			while True:
				data = connection.recv(1024)
#				print('received {!r}'.format(data))
				lock.acquire()
				controlJson = data
				lock.release()
#				print(controlJson)
				if data:
#					print('sending data back to the client')
					connection.sendall(data)
				else:
#					print('no data from', client_address)
					break
		finally:
            # Clean up the connection
			connection.close()

def carControl():
	global controlJson

	gpio.setmode(gpio.BOARD)
	gpio.setwarnings(False)

	# Setting LED's
	lPosterior1 = 18
	lPosterior2 = 19
	gpio.setup(lPosterior1,gpio.OUT)
	gpio.setup(lPosterior2,gpio.OUT)

	lTrasera1 = 29
	lTrasera2 = 31
	gpio.setup(lTrasera1,gpio.OUT)
	gpio.setup(lTrasera2,gpio.OUT)

	lReversa1 = 22
	lReversa2 = 23
	gpio.setup(lReversa1,gpio.OUT)
	gpio.setup(lReversa2,gpio.OUT)

	# Setting Motor 1
	motor1_f = 8
	motor1_b = 10
	gpio.setup(motor1_f, gpio.OUT)
	gpio.setup(motor1_b, gpio.OUT)

	motor1_forward = gpio.PWM(motor1_f, 50)
	motor1_backward = gpio.PWM(motor1_b, 50)

	#Setting Motor 2
	motor2_f = 12
	motor2_b = 16
	gpio.setup(motor2_f, gpio.OUT)
	gpio.setup(motor2_b, gpio.OUT)

	motor2_forward = gpio.PWM(motor2_f, 50)
	motor2_backward = gpio.PWM(motor2_b, 50)
	while True:
		control = '{}'
		lock.acquire()
		control = json.loads(str(controlJson))
		lock.release()

		if len(control)>0:
			print(control)
			estado = control["estado"]
			direccion = control["direccion"]
			lPosteriores = int(control["luces"]["posteriores"])
			lTraseras = int(control["luces"]["traseras"])
			if lPosteriores == 1:
				gpio.output(lPosterior1,gpio.HIGH)
				gpio.output(lPosterior2,gpio.HIGH)
				# Encender luces posteriores
			else:
				gpio.output(lPosterior1,gpio.LOW)
				gpio.output(lPosterior2,gpio.LOW)
			if lTraseras == 1:
				# Encender luces traseras
				gpio.output(lTrasera1,gpio.HIGH)
                                gpio.output(lTrasera2,gpio.HIGH)
                                # Encender luces posteriores
                        else:
                                gpio.output(lTrasera1,gpio.LOW)
                                gpio.output(lTrasera2,gpio.LOW)
			if estado == "avanzar":
				gpio.output(lReversa1,gpio.LOW)
				gpio.output(lReversa2,gpio.LOW)

				motor1_forward.stop()
				motor2_forward.stop()
				motor1_backward.stop()
				motor2_backward.stop()
				time.sleep(0.1)
				if direccion == "vertical":
					motor1_forward.start(50)
					motor2_forward.start(50)
				elif direccion == "izquierda":
					motor1_backward.start(50)
					motor2_forward.start(50)
				elif direccion == "derecha":
					motor1_forward.start(50)
					motor2_backward.start(50)
			elif estado == "detener":
				# Apagar motores
				gpio.output(lReversa1,gpio.LOW)
                                gpio.output(lReversa2,gpio.LOW)

                                motor1_forward.stop()
                                motor2_forward.stop()
                                motor1_backward.stop()
                                motor2_backward.stop()
			elif estado == "reversa":
				# Encender luces de reversa
				gpio.output(lReversa1,gpio.HIGH)
                                gpio.output(lReversa2,gpio.HIGH)

                                motor1_forward.stop()
                                motor2_forward.stop()
                                motor1_backward.stop()
                                motor2_backward.stop()
				if direccion == "vertical":
					motor1_backward.start(50)
                                        motor2_backward.start(50)
				elif direccion == "izquierda":
					motor1_backward.start(50)
                                        motor2_forward.start(50)
				elif direccion == "derecha":
					motor1_forward.start(50)
                                        motor2_backward.start(50)

if __name__=="__main__":
	threads = []

	tCarControl = Thread(target=carControl)
	threads.append(tCarControl)
	tCarControl.start()

	tSocket = Thread(target=socketCommunication)
	threads.append(tSocket)
	tSocket.start()


