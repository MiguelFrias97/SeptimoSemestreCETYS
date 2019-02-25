import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.12.18.16', 9000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'{"estado":"detener","direccion":"vertical","posteriores":"0","traseras":"1"}'
    print('sending {!r}'.format(message))
    sock.sendall(message)
finally:
    print('closing socket')
    sock.close()
