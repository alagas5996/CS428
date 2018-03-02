# UDP Pinger - Client

from socket import *

#Tracks number of pongs recieved
recievedBack = False

#Gets port number
port = 0
while(port == 0):
    try:
        port = int(input("Input port number: "))
    except:
        print("Port can only be an integer.")

#Gets client name
cliName = '0'
while(cliName == '0'):
    try:
        cliName = input("Input client name: ")
    except:
        print("Must enter a client name")

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Assign IP address and port number to socket
clientSocket.bind(('localhost', port))
clientSocket.settimeout(10)

#Send server a message
clientSocket.connect(('localhost', 4265))
message = 'NULL'

# Receive the server packet along with the address it is coming from
try:
    clientSocket.send(str(cliName).encode())
    message = clientSocket.recv(1024).decode("ascii")
    recievedBack = True

#If socket times out
except timeout:
    print('Failure: Timeout')

#Test for failure to connect
if recievedBack:
    print('Sent message to server: %s' %cliName)
    print('Recieved from server: %s' %message)
else:
    print("Failure: no response recieved")

#Close the socket
clientSocket.close()
