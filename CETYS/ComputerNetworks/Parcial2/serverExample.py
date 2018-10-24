from functionsServer import *

s = createSocket(50000,"")
conn,addr = stablishConnection(s)
receiveData(conn)
sendFile(conn,'server.py')
disconnect(conn)
