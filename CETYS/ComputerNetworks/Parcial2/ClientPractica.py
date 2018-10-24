import time
from functionsClient import *

port = 50000
host = "10.12.18.139"
bufferSize = 1024

s = createSocket(port,host)
receiveData(s,bufferSize)
data = raw_input()
sendData(s,data)
receiveData(s,bufferSize)
receiveData(s,bufferSize)
filename = raw_input()
sendData(s,filename)
receiveFile(s,filename)
#sendData(s,"File Received")

disconnect(s)
