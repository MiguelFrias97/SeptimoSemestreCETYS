import socket

TCP_IP = "10.0.0.1"
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print "Connection address: ", addr 

while 1:
	data_recv = conn.recv(BUFFER_SIZE)
	data = "HTTP Error 418"
	if not data_recv: break
	print data_recv
	conn.send(data)
conn.close()
