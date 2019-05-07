from socket import *

serverName = 'hostname'
serverPort = 12000
# AF_INET indicates the underlying network is using IPv4
# SOCK_DGRAM indicates a UDP socket is used
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
# 2048 is the buffer size, which works for most purposes
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
