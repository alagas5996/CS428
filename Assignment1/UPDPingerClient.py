# UDP Pinger - Client

from socket import *
import time

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
clientSocket.bind(('localhost', 10000))
clientSocket.settimeout(1)

#Tracks number of pongs recieved
recievedBack = 0
totalTime = 0

#Ping server 10x
for i in range(0, 10):
    #Time response
    start = time.time()
    
    # Ping the server
    clientSocket.sendto('Ping'.encode(), ('localhost', 12000))

    # Receive the server packet along with the address it is coming from
    try:
        clientSocket.recvfrom(1024)
        end = time.time()
        pingTime = (end - start)
        print("Ping %d: %f sec" %((i + 1), pingTime))
        totalTime += pingTime
        recievedBack += 1
    #If socket times out
    except timeout:
        print('Ping %d: Timeout' %(i + 1))

#Failed to connect
if (recievedBack == 0):
    print("Ping failed: no responses recieved")

#Successful connection
else:
    averageTime = totalTime / recievedBack
    print("Average ping: %f sec\n" %averageTime)
