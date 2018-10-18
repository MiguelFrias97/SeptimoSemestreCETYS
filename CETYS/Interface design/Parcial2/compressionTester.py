import RPi.GPIO as gpio
import smbus
import time
import json
import time

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

	if gpio.input(startPin):
		id = counter()
		print('iniciar Sample')
		tensionData = []
		compresionData = []
		desplazamientoData = []
		data = {}
		start = time.time()
		while True:
			if gpio.input(stopPin) == 1:
				break
			# Leer sensor tension
			bus.write_byte(address,a0)
			value = bus.read_byte(address)
			tensionOut = (vRef*value)/255
			tensionData.append(tensionOut)
			#print(tensionOut)
#			time.sleep(0.1)

			# Leer sensor Compresion
#			bus.write_byte(address, a1)
#			value = bus.read_byte(address)
#			compresionOut = (vRef*value)/255
#			compresionData.append(compresionOut)
#			print(compresionOut)
#			time.sleep(0.1)

			# Leer sensor Desplazamiento
			bus.write_byte(address,a2)
			value = bus.read_byte(address)
			desplazamientoOut = (vRef*value)/255
			desplazamientoData.append(desplazamientoOut)
#			print(desplazamientoOut)
#			time.sleep(0.1)

			time.sleep(0.1)
			#print ("")

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
