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
material = "111"

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
        global material
	# Setting GPIO
	gpio.setmode(gpio.BOARD)
	gpio.setwarnings(False)

	# Voltaje de referencia para regla de tres
	vRef = 8

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

	vfoff = 5.15
	av = 470
	forceConstant = 33.88

	while True:
		if startR:
                        print "Starting Test"
#		if gpio.input(startPin):
			id = counter()
			print('iniciar Sample')
			tensionData = []
			compresionData = []
			desplazamientoData = []
			data = {}
			start = time.time()
			while True:
				if stopR:
#				if gpio.input(stopPin):
					break
				# Leer sensor tension
				bus.write_byte(address,a0)
				value = bus.read_byte(address)
				tensionOut = (vRef*value)/255.0
				tensionOut = ((tensionOut-vfoff)/av)*1000*forceConstant
#				tensionData.append(value)
				tensionData.append(tensionOut)

				# Leer sensor Desplazamiento
				bus.write_byte(address,a1)
				value = bus.read_byte(address)
				desplazamientoOut = (vRef*value)/255.0
				desplazamientoOut = (desplazamientoOut*4)/8
#				desplazamientoData.append(value)
				desplazamientoData.append(desplazamientoOut)

				time.sleep(0.1)
			lock.acquire()
			startR = False
			stopR = False
			lock.release()
			print('preparando para enviar')
			final = time.time()
			timePassed = final - start
			data['id'] = material + str(id)
			data['date']=datetime.datetime.now().strftime("%d/%-m/%Y %H:%M:%S")
			data['strain'] = tensionData
			data['displacement'] = desplazamientoData

			data2send = json.dumps(data)
			headers={'Content-Type':"application/json"}
			print(data2send)
                        
			response= requests.request("POST",url=endpoint,data=data2send,headers=headers)
			print(response)
                        print(data["id"])
def requestAPI(endpoint):
	global startR
	global stopR
        global material
	while True:
		r = requests.get(url=endpoint)
		data = json.loads(str(r.text))
		# TODO: Finish filename and state readings from json GET request
		testState = int(data["TestState"])
		material = data["Material"]
                print(material)
                lock.acquire()
		if testState == 1:
			startR = True
			stopR = False
		elif testState == 0:
			stopR = True
			startR = False
		lock.release()

		time.sleep(0.1)


if __name__=="__main__":
	endpoint = 'http://10.12.10.191/API/Test'

	threads = []

	tRequest = Thread(target=requestAPI,args=(endpoint,))
	threads.append(tRequest)
	tRequest.start()

	tRead = Thread(target=readSensor,args=('http://10.12.10.191/API/Sensors',))
	threads.append(tRead)
	tRead.start()

