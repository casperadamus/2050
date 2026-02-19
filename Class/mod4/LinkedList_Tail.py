class Node:
    def __init__(self, data, _next = None): # O(1)
        self.data = data   # This node *has* this data
        self._next = _next # This serves as a link to the next node

    def __str__(self): # O(1)
        return "Node.data = {}".format(self.data)


class LinkedList:
    def __init__(self):     # O(1)
        self._head = None   # First item in LinkedList
        self._tail = None   # Last item in LinkedList
        self._len = 0

    def add_first(self, data):  # O(1)
        self._head = Node(data, self._head)
        self._len += 1
        if len(self) == 1: self._tail = self._head # Edge case: add_first to empty LinkedList

    def remove_first(self): # O(1)
        if len(self) == 0: raise RuntimeError("Attempt to remove_first from empty LinkedList") # Edge case: remove_first from empty LL        
        # Update _head to _head._next
        # Return data from old _head

        data = self._head.data
        
        self._head = self._head._next
        
        self._len -= 1

        if len(self) == 0: self._tail = None
        
        return data

    def add_last(self, data): # O(1)
        if self._head is None: return self.add_first(data)   # Edge case: add_last to empty LL 

        # Create a new node: data=data, _next = None
        # Update the old last node: _next = new_node
        self._tail._next = Node(data)
        
        self._tail = self._tail._next

        self._len += 1



    def remove_last(self): # O(n)
        if len(self) == 0: raise RuntimeError("Attempt to remove_last from empty LinkedList") # Edge case: remove_last from empty LL
        if len(self) == 1: return self.remove_first() # Edge case: remove_last from single item LL


        # Find penultimate node
        # Get data from lat node
        # delete last node: update penultimate node to point to None
        # return data

        penultimate_node = self._head
        while penultimate_node._next._next is not None:
            penultimate_node = penultimate_node._next # Moves forward one step in LL

        data = self._tail.data

        penultimate_node._next = None
        self._tail = penultimate_node

        self._len -= 1

        return data

    def __len__(self): # O(1)
        return self._len

    def __str__(self): # O(n)
        return_str = 'head: '
        current_node = self._head
        while current_node is not None:
            return_str += str(current_node.data) + ' --> '
            current_node = current_node._next
        return_str = return_str[:-5]
        return_str += ' :tail'
        return return_str

if __name__ == '__main__':
    ### Test Node class
    n = Node(3)
    assert(str(n) == "Node.data = 3")

    ### Test add_first and remove_last
    ll = LinkedList()
    for i in range(10): ll.add_first(i)
    print(ll)
    for i in range(10): assert(ll.remove_last() == i)


    ### Test add_last and remove_first
    ll = LinkedList()
    for i in range(10): ll.add_last(i)
    for i in range(10): assert(ll.remove_first() == i)

    ### Test remove_first and remove_last from empty list
    ll = LinkedList()
    try:
        ll.remove_first()
        raise Exception("Attempt to remove_first from empty list did not raise RuntimeError")        
    except RuntimeError:
        pass

    ll = LinkedList()
    try:
        ll.remove_last()
        raise Exception("Attempt to remove_last from empty list did not raise RuntimeError")        
    except RuntimeError:
        pass