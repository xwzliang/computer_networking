from socket import *

# The "welcoming socket" that waits for connection-establishment requests from TCP clients
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
# number 1 specifies the maximum number of queued connections (at least 1)
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    # The server process creates a new socket for actual data transmission
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
