from linked_lists import *
def addres(connectionSocket, version, status, rfc_num, title, host, port):
    connectionSocket.send(version+" "+status+"\n"+"RFC "+rfc_num+" "+title+" "+host+" "+port)
    
