import socket


TCP_IP = '10.12.18.16'
TCP_PORT = 9000
BUFFER_SIZE = 1024
MESSAGE = "h"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
