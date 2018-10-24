import socket
import subprocess as sbp

def createSocket(port,host):
    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
    return s

def stablishConnection(s):
    conn = None;
    while conn == None:
        conn, addr = s.accept()  # Establish connection with client.
    print('Got connection from', addr)
    return conn,addr

def receiveData(conn):
    data = None
    while data == None:
        data = conn.recv(1024)
    print('Server received', repr(data))
    #print(data)
    return data

def sendData(conn,data):
    conn.send(data)

def sendFile(conn,filename):
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        print('Sent ', repr(l))
        l = f.read(1024)
    f.close()
    print("Done Sending")

def disconnect(conn):
    conn.send('Thank you for connecting')
    conn.close()

def executeBashCommand(command):
    process = sbp.Popen(command.split(), stdout=sbp.PIPE)
    out,error = process.communicate()
    return out
