class node_peer(object):
    def __init__(self, hostname, port_number, next = None):
        self.hostname = hostname
        self.port_number = port_number
        self.next = next
    def get_nextPeer(self):
        return self.next
    def set_nextPeer(self, next):
        self.next = next
    def get_hostnamePeer(self):
        return self.hostname
    def get_portnumber(self):
        return self.port_number
        
        
        
class linked_list_peer(object):
    def __init__(self):
        self.head_peer = None
    def set_head_peer(self, head_peer):
        self.head_peer = head_peer
    def get_head_peer(self):
        return self.head_peer
    def get_portOfHost(self, hostname):
        head = self.head_peer
        while head != None:
            if head.get_hostnamePeer() == hostname:
                return head.getportnumber()
            head = head.get_nextPeer()
    
    def add_peer(self, hostname, port_number):
        new_peer = node_peer(hostname, port_number)
        new_peer.set_nextPeer(self.head_peer)
        self.head_peer = new_peer
    def del_peer(self, hostname):
        curr = self.head_peer
        prev = None
        while curr:
            if curr is None:
                break
            if curr.get_hostnamePeer() == hostname:
                if prev is None:
                    self.head_peer = curr.get_nextPeer()
                else:
                    prev.set_nextPeer(curr.get_nextPeer())
            else:
                prev = curr
                curr = curr.get_nextPeer()
                
        
        
class node_RFC(object):
    def __init__(self, RFC_number, title, hostname, next= None):
        self.RFC_number = RFC_number
        self.title = title
        self.hostname = hostname
        self.next = next
    def set_nextRFC(self, next):
        self.next = next
    def get_nextRFC(self):
        return self.next
    def get_RFC_number(self):
        return self.RFC_number
    def get_RFC_title(self):
        return self.title
    def get_hostname(self):
        return self.hostname
    
class linked_list_RFC(object):
    def __init__(self):
        self.head_RFC = None
        
    def set_head_RFC(self, head_RFC):
        self.head_RFC = head_RFC
        
    def get_head_RFC(self):
        return self.head_RFC
        
    def get_hostnameRFC(self):
        return self.hostname
        
    def add_RFC(self, RFC_number, title, hostname):
        new_RFC = node_RFC(RFC_number, title, hostname)
        new_RFC.set_nextRFC(self.head_RFC)
        self.head_RFC = new_RFC
        
    def traverse_RFC(self, connectionSocket, version):
    #traverse the list and for every node send the node's data to client
        head = get_head_RFC()
        flag = 0
        if head == None:
            status = "404 Not Found"
            connectionSocket.send(version+" "+status+"\n")
            return
        while head != None:
            status = "200 OK"
            if flag == 0:
                connectionSocket.send(version+" "+status+"\n")
            flag = 1
            headpeer = linked_list_peer()
            connectionSocket.send("RFC "+head.get_RFC_number()+" "+head.get_RFC_title()+" "+head.get_hostname()+" "+headpeer.get_portOfHost(head.get_hostname())+"\n")
            head = head.get_nextRFC()
    def search_RFC(self, connectionSocket, version, rfc_num, title):
        # need to add this function according to further requirements
        head = get_head_RFC()
        flag = 0
        if head == None:
            status = "404 Not Found"
            connectionSocket.send(version+" "+status+"\n")
            return
        while head != None:
            if head.get_RFC_number() != rfc_num:
                head = head.get_nextRFC()
                continue
            if flag == 0:
                connectionSocket.send(version+" "+status+"\n")
            flag = 1
            headpeer = linked_list_peer()
            connectionSocket.send("RFC "+head.get_RFC_number()+" "+head.get_RFC_title()+" "+head.get_hostname()+" "+headpeer.get_portOfHost(head.get_hostname())+"\n")
            head = head.get_nextRFC()
        
    def del_RFC(self, hostname):
        curr = self.head_RFC
        prev = None
        while curr:
            if curr is None:
                break
            if curr.get_hostnameRFC == hostname:
                if prev is None:
                    self.head_RFC = curr.get_nextRFC()
                else:
                    prev.set_nextRFC(curr.get_nextRFC())
            else:
                prev = curr
                curr = curr.get_nextRFC()
