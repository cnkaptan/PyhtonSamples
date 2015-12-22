import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(("www.py4inf.com", 80))

mySocket.send("GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n")

while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break
    print data

mySocket.close()
