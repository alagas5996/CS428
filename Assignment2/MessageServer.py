# UDP Pinger

# Must have this server running before you can run the UDP Pinger Client code

from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign IP address and port number to socket
serverSocket.bind(('localhost', 4265)) #localhost can be replaced by I.P address

while True:
    #Accept connection
    serverSocket.listen(2)
    conn1, address1 = serverSocket.accept()
    port1 = address1[1]
    message1 = conn1.recv(1024).decode("ascii")
    print('Connection recieved, name is: %s' %message1)
    serverSocket.listen(2)
    conn2, address2 = serverSocket.accept()
    message2 = conn2.recv(1024).decode("ascii")
    print('Connection recieved, name is: %s' %message2)

    #Construct message
    messageBack = '%s recieved before %s' %(message1, message2)
    
    #Server responds
    conn1.send(messageBack.encode())
    conn2.send(messageBack.encode())
    print('Sent acknowledgment to both %s and %s' %(message1, message2))
