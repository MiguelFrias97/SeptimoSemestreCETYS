from threading import *

import json
import time
import socket
import sys

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
	while True:
		control = '{}'
		lock.acquire()
		control = json.loads(str(controlJson))
		lock.release()

		if len(control)>0:
			print(control)
			estado = control["estado"]
			direccion = control["direccion"]
			lPosteriores = control["luces"]["posteriores"]
			lTraseras = control["luces"]["traseras"]
			if lPosteriores:
				pass
				# Encender luces posteriores
			elif lTraseras:
				pass
				# Encender luces traseras
			if estado == "avanzar":
				if direccion == "vertical":
					pass
				elif direccion == "izquierda":
					pass
				elif direccion == "derecha":
					pass
			elif estado == "detener":
				# Apagar motores
			elif estado = "reversa":
				# Encender luces de reversa
				if direccion == "vertical":
					pass
				elif direccion == "izquierda":
					pass
				elif direccion == "derecha":
					pass

if __name__=="__main__":
	threads = []

	tCarControl = Thread(target=carControl)
	threads.append(tCarControl)
	tCarControl.start()

	tSocket = Thread(target=socketCommunication)
	threads.append(tSocket)
	tSocket.start()


