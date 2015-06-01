from socket import *
servername = 'name'
serverport = 7734
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(servername, serverport)

//ask for input from the user
print('Use 1.ADD for adding a new RFC \n 2.LOOKUP for finding RFC \n 3.LIST for list of all the available RFC's.')
function = raw_input('enter function')
if function != "LIST":
    rfc = raw_input('enter RFC nuumber')
    title = raw_input('enter title')
version = raw_input('enter version like P2P-CI/1.0')
host = raw_input('enter host name')
port = raw_input('enter ur port')
#send the infrmation to the server
if function != "LIST":
    clientSocket.send(function+' '+'RFC '+rfc+' '+version+"\n"+"HOST: "+host+"\n"+"PORT: "+port+"\n"+"TITLE: "+title)
clientSocket.send(function+' '+'ALL'+' '+version+"\n"+"HOST: "+host+"\n"+"PORT: "+port)
result = clientSocket.recv(1024)
#open connection with the peer.. using the data in result variable
line = result.split("\n")
version, a , b = line[0].split(" ")
status = a+b
if status == "200 OK"
    #open connection with peer and do the things
    start = line[1].find('RFC: ')+5
    end = line[1].find(' ', start)
    rfc_num = line[1][start:end]
    port = line[1][-4:]
    start = end + 1
    end = line[1].find(port)-1
    r = line[1][start:end]
clientSocket.close()
