from socket import *
import os
serverPort = 7734
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind('',serverPort)
serverSocket.listen(4)
print 'Server is up and listening'
while 1:
    //accept function accepts a connection request from a client and assigns the new connection socket to connectionSocket
    // and assigns the ip and port of the lient to the resp. variables
    connectionSocket, (clientip, clientport) = serverSocket.accept()
    //getting client's name from its ip
    clientname = connectionSocket.gethostbyaddr(clientip)
    
    if os.fork() == 0:
          serverSocket.close()
          implement_child(); //to do
          exit(0)
    connectionSocket.close()
