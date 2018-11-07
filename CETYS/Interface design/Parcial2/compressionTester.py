import RPi.GPIO as gpio
import smbus
import time
import json
import datetime
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

def readSensor(endpoint):
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
			data['id']= id
			#data['timePassed'] = timePassed
			data['date']=datetime.datetime.now().strftime("%d/%-m/%Y %H:%M:%S")
			data['strain'] = tensionData
			#data['compresion'] = compresionData
			data['displacement'] = desplazamientoData

			data2send = json.dumps(data)
			headers={'Content-Type':"application/json"}
			print(data2send)

			response= requests.request("POST",url=endpoint,data=data2send,headers=headers)
			print(response)

def requestAPI(endpoint):
	global startR
	global stopR
	while True:
		r = requests.get(url=endpoint)
		data = int(r.text[1:2])
		lock.acquire()
		print(startR)
		if data == 1:
			startR = True
			stopR = False
		elif data == 0:
			stopR = True
			startR = False
		print(startR)
		lock.release()

		time.sleep(0.1)

if __name__=="__main__":
	#endpoint =' https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22tijuana%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
	endpoint = 'http://10.12.10.191/API/Test'

#	startR = False
#	stopR = False
#	lock = Lock()

	threads = []

	tRequest = Thread(target=requestAPI,args=(endpoint,))
	threads.append(tRequest)
	tRequest.start()

	threads = []
	tRead = Thread(target=readSensor,args=('http://10.12.10.191/API/Sensors',))
	threads.append(tRead)
	tRead.start()

#	if gpio.input(startPin):
#		for thread in threads:
#			thread.join()
#
