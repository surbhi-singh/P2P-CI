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
        
        
        
class linked_list_peer(object):
    def __init__(self, head_peer = None):
        self.head_peer = head_peer
        
        
        
class linked_list_RFC(object):
    def __init__(self, head_RFC = None):
        self.head_RFC = head_RFC
        
        
        
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
    
