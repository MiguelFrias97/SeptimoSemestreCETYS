import bluetooth

bd_addr = "B8:27:EB:9A:2E:7D"

port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
