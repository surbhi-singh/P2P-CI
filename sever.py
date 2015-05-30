from socket import *
import os
from linked_lists import *
serverPort = 7734
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind('',serverPort)
serverSocket.listen(4)
newpeer = linked_list_peer()
rfcadder = addRFC()
print 'Server is up and listening'
while 1:
    #accept function accepts a connection request from a client and assigns the new connection socket to 
    # connectionSocket and assigns the ip and port of the lient to the resp. variables
    connectionSocket, (clientip, clientport) = serverSocket.accept()
    #getting client's name from its ip
    clientname = connectionSocket.gethostbyaddr(clientip)
    #add this peer to the linked list
    newpeer.add_peer(clientname, clientport)
    if os.fork() == 0:
          serverSocket.close()
          implement_child(connectionSocket); #to do..dnt forget to delete the peer's node from the linked list after the work is done.
          newpeer.del_peer(clientname)
          exit(0)
    connectionSocket.close()
def implement_child(connectionSocket):
    result = connectionSocket.recv(1024)
    for line in result.split("\n"):
        if "ADD" in line:
            #Do ADD functionality
            for word in result.split(" "):
                
        else if "LIST" in line:
            #Do LIST functionality
        else:
            #Do LOOKUP functionality
