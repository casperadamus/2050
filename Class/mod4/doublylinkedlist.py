class Node:
    def __init__(self, data, prev=None, link=None):
        """Initializes a new node"""
        self.data = data
        self.prev = prev
        self.link = link
        

    def __repr__(self):
        return f"Node({self.data})"
    
class DoublyLinkedList:
    def __init__(self, items=None):
        self._head = None
        self._tail = None
        self._len = 0

        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        return self._len
    
    def get_head(self):
        return self._head
    
    def get_tail(self):
        return self._tail
    
    def add_first(self, data):
        self._head = Node(data, prev=None, link=self._head)
        
        if len(self) == 0: self._tail = self._head

        else:
            self._head.link.prev = self._head
        
        self._len += 1

    def add_last(self, data):
        self._tail = Node(data, prev=self._tail, link=None)

        if len(self) == 0: self._head = self._tail

        else:
            self._tail.prev.link = self._tail

        self._len += 1

    def remove_first(self):
        if len(self) == 0:
            raise IndexError("Cannot remove from empty DLL.")
        
        # Remove data
        data = self._head.data

        # update list
        if len(self) == 1:
            self._head = None
            self._tail = None

        else:
            if self._head.link is None:
                pass
            self._head = self._head.link
            self._head.prev = None

        self._len -= 1


        # Return data
        return data

    def remove_last(self):
        if len(self) == 0:
            raise IndexError("Cannot remove from empty DLL.")
        
        # Remove data
        data = self._tail.data

        # update list
        if len(self) == 1:
            self._head = self._tail = None

        else:
            self._tail = self._tail.prev
            self._tail.link = None

        self._len -= 1

        # Return data
        return data