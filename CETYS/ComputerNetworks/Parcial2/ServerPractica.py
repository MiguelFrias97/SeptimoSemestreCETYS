import time
from functionsServer import *

host = ""

def sendingFile(port):
	s = createSocket(port,host)
	conn,addr = stablishConnection(s)
	sendData(conn,"Esperando el comando: ")
	command = receiveData(conn)
	rCommand = executeBashCommand(command)
	sendData(conn,rCommand)
	sendData(conn,"Nombre del archivo deseado(extension explicita):")
	filename = receiveData(conn)
	sendFile(conn,filename)
	disconnect(conn)
	conn = None
	addr = None
	s = None

def again(port):
	s = createSocket(port,host)
	conn,addr = stablishConnection(s)
	sendData(conn,'Quieres recibir otro archivo(y/n):')
	answer = receiveData(conn)
	disconnect(conn)
	s = None
	conn = None
	addr = None
	return answer

if __name__=="__main__":
	ports = [50000,8000,9000,8001,8080,51000]
	port = 8000
	index = 0
	index2 = -1
	while True:
		sendingFile(ports[index])
		time.sleep(1)
		index += 1
		if index > len(ports)-1:
			index = 0
		answer = again(ports[index2])
		time.sleep(0.5)
		index2 -= 1
		if index2  < -1*(len(ports)-1):
			index2 = -1
		if answer!='y':
			break
