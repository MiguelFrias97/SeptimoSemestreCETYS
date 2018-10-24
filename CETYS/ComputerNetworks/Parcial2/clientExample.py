from functionsClient import *

s = createSocket(50000,"10.12.18.139")
sendData(s,"Hello Server!")
receiveFile(s)
disconnect(s)
