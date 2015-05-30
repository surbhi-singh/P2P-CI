from socket import *
servername = 'name'
serverport = 7734
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(servername, serverport)

//ask for input from the user


clientSocket.send(sentence)
result = clientSocket.recv(1024)
//open connection with the peer.. using the data in result variable
clientSocket.close()
