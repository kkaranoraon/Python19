#!/usr/bin/env python2
import socket

 
serverAddressPort1   = ("127.0.0.1", 20001)

serverAddressPort2   = ("127.0.0.1", 20002)

bufferSize          = 1024

# Send to server using created UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while 3>2 :
	msgFromClient       = raw_input("type your message :  ")
	bytesToSend         = str.encode(msgFromClient)
	


	UDPClientSocket.sendto(bytesToSend, serverAddressPort1)
	UDPClientSocket.sendto(bytesToSend, serverAddressPort2)
	msgFromServer = UDPClientSocket.recvfrom(bufferSize)
	msg = "Message from Server {}".format(msgFromServer[0])
	print(msg)
# Create a UDP socket at client side



 


