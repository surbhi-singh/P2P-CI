from socket import *
import os
import re
import sendResponse
from linked_lists import *
serverPort = 7734
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind('',serverPort)
serverSocket.listen(4)
newpeer = linked_list_peer()
rfcadder = linked_list_RFC()
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
          implement_child(connectionSocket, clientname, clientport); #to do..dnt forget to delete the peer's node from the linked list after the work is done.
          newpeer.del_peer(clientname)
          exit(0)
    connectionSocket.close()
def implement_child(connectionSocket, host, port):
    result = connectionSocket.recv(1024)
    line = result.split("\n"):
    if "ADD" in line[0]:
        #Do ADD functionality
        start = line[0].find('RFC: ') + 5
        end = line[0].find(' ', start)
        rfc_num = line[0][start:end]
        start = line[3].find('TITLE: ')+7
        title = line[3][start:]
        start = line[0].find(rfc_num)
        end = line[0].find(' ', start)
        start = end + 1
        version = line[0][start:]
        # if this approach doent wrk for searching then use this:
        #rfc_num = re.search('RFC: (.+?) ', line[0]).group(1)
        #title = re.search('TITLE: (.+?)\n', line[3]).group(1)
        rfcadder.add_RFC(rfc_num, title, host)
        status = "200 OK"
        sendResponse.addres(connectionSocket, version, status, rfc_num, title, host, port)
                
    else if "LIST" in line[0]:
        #Do LIST functionality
        start = line[3].find('TITLE: ')+7
        title = line[3][start:]
        start = line[0].find(rfc_num)
        end = line[0].find(' ', start)
        start = end + 1
        version = line[0][start:]
        #define status
        connectionSocket.send(version+" "+status+"\n")
        rfcadder.traverse_RFC()
        
    else:
        #Do LOOKUP functionality
        start = line[0].find('RFC: ') + 5
        end = line[0].find(' ', start)
        rfc_num = line[0][start:end]
        start = line[3].find('TITLE: ')+7
        title = line[3][start:]
        start = line[0].find(rfc_num)
        end = line[0].find(' ', start)
        start = end + 1
        #define status
        version = line[0][start:]
        rfcadder.search_RFC()
