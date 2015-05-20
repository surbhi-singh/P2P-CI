from socket import *
import os
serverPort = 7734
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind('',serverPort)
serverSocket.listen()
print 'Server is up and listening'
while 1:
    connectionSocket, clientaddress = serverSocket.accept()
    if os.fork() == 0:
          serverSocket.close()
          implement_child(); //to do
          exit(0)
    connectionSocket.close()
