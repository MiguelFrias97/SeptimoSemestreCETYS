import time
from functionsClient import *

#host = "192.168.1.67" #casa
host = "10.12.18.139" #cetys
bufferSize = 1024

def receivingFile(port,host,bufferSize):
	s = createSocket(port,host)
	receiveData(s,bufferSize)
	data = raw_input()
	sendData(s,data)
	receiveData(s,bufferSize)
	receiveData(s,bufferSize)
	filename = raw_input()
	sendData(s,filename)
	receiveFile(s,filename)
	disconnect(s)
	s = None

def again(port,host,bufferSize):
	s = createSocket(port,host)
	receiveData(s,bufferSize)
	answer = raw_input()
	sendData(s,answer)
	disconnect(s)
	s = None
	return answer

if __name__=="__main__":
	ports = [50000,8000,9000,8001,8080,51000]
	index = 0
	index2 = -1
	while True:
		receivingFile(ports[index],host,bufferSize)
		time.sleep(1)
		index += 1
		if index > len(ports)-1:
			index = 0
		answer = again(ports[index2],host,bufferSize)
		time.sleep(1)
		index2 -= 1
		if index2 < -1*(len(ports)-1):
			index2 = -1
		if answer != 'y':
			break
