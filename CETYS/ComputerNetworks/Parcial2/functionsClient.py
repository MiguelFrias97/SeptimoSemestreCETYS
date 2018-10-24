import socket

def createSocket(port,host):
    try:
        s = socket.socket()
        s.connect((host,port))
        return s
    except:
        print('Socket created.')

def receiveFile(s,filename):
    try:
        with open(filename, 'wb') as f:
            print ('file opened')
            while True:
                print('receiving data...')
                data = s.recv(1024)
                print('data=%s', (data))
                if not data:
                    break
                # write data to a file
                f.write(data)

        f.close()
        print('Successfully get the file')
    except:
        print("Error receiving file")

def sendData(s,data):
    s.send(data)

def receiveData(s,bufferSize):
    data = None
    while data == None:
        data = s.recv(bufferSize)
    print (data)
    return data

def disconnect(s):
    s.close()
    print('Connection Closed')


