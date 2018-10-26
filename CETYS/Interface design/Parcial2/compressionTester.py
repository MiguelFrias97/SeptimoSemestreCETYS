import RPi.GPIO as gpio
import smbus
import time
import json
import time
import requests

from threading import *

startR = False
stopR = False
lock = Lock()

def counter():
	try:
		with open("api.txt","r+") as f:
			value = int(f.read())
			f.seek(0)
			f.write(str(value + 1))
		f.close()
	except:
		f = open("api.txt",'w')
		value = 1
		f.write(str(value))
		f.close()
	return value

def readSensor():
	global startR
	global stopR
	# Setting GPIO
	gpio.setmode(gpio.BOARD)
	gpio.setwarnings(False)

	# Voltaje de referencia para regla de tres
	vRef = 5

	# Direccion del dispositivo i2c
	address = 0x48

	# Direcciones sensores
	# Tension
	a0 = 0x40
	# Compresion
	a1 = 0x41
	# Desplazamiento
	a2 = 0x42
	## a3 = 0x43

	# Setting bit de inicio y baja
	startPin = 37
	stopPin = 38
	gpio.setup(startPin, gpio.IN)
	gpio.setup(stopPin, gpio.IN)

	bus = smbus.SMBus(1)

	while True:
		#print("Lectura de sensor: ",startR)
		if startR:
			id = counter()
			print('iniciar Sample')
			tensionData = []
			compresionData = []
			desplazamientoData = []
			data = {}
			start = time.time()
			while True:
				#lock.acquire()
				#lock.release()
				if stopR:
					break
				# Leer sensor tension
				bus.write_byte(address,a0)
				value = bus.read_byte(address)
				tensionOut = (vRef*value)/255
				tensionData.append(tensionOut)
				#print(tensionOut)
#				time.sleep(0.1)

				# Leer sensor Compresion
#				bus.write_byte(address, a1)
#				value = bus.read_byte(address)
#				compresionOut = (vRef*value)/255
#				compresionData.append(compresionOut)
#				print(compresionOut)
#				time.sleep(0.1)

				# Leer sensor Desplazamiento
				bus.write_byte(address,a2)
				value = bus.read_byte(address)
				desplazamientoOut = (vRef*value)/255
				desplazamientoData.append(desplazamientoOut)
#				print(desplazamientoOut)
#				time.sleep(0.1)

				time.sleep(0.1)
				#print ("")
			lock.acquire()
			startR = False
			stopR = False
			lock.release()
			print('preparando para enviar')
			final = time.time()
			timePassed = final - start
			data['testId']= id
			data['timePassed'] = timePassed
			data['tension'] = tensionData
			data['compresion'] = compresionData
			data['desplazamiento'] = desplazamientoData

			data2send = json.dumps(data)
			print(data2send)

def requestAPI(endpoint):
	global startR
	global stopR
	r = requests.get(url=endpoint)
	data = r.json()
	print(data['query']['results']['channel']['location']['city'])
	lock.acquire()
	print(startR)
	if data['query']['results']['channel']['location']['city']  == 'Tijuana':
		startR = True
	print(startR)
	lock.release()

	time.sleep(5)

	endpoint = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22nome%2C%20ak%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
	r = requests.get(url=endpoint)
	data = r.json()
	print(data['query']['results']['channel']['location']['city'])
	lock.acquire()
	print(stopR)
	if data['query']['results']['channel']['location']['city']!='Tijuana':
		stopR = True
	print(stopR)
	lock.release()
		# Obtener el valor de startR y stopR

if __name__=="__main__":
	endpoint =' https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22tijuana%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

#	startR = False
#	stopR = False
#	lock = Lock()

	threads = []

	tRequest = Thread(target=requestAPI,args=(endpoint,))
	threads.append(tRequest)
	tRequest.start()

	threads = []
	tRead = Thread(target=readSensor)
	threads.append(tRead)
	tRead.start()

#	if gpio.input(startPin):
#		for thread in threads:
#			thread.join()
#
