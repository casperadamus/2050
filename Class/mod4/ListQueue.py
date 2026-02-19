class ListQueue:
    def __init__(self):         # O(1)
        self._L = []

    def enqueue(self, item):    # O(1)
        self._L.append(item)

    def dequeue(self):          # O(n)       
        return self._L.pop(0)

    def __len__(self):          # O(1)
        return len(self._L)
        
    def isempty(self):              # O(1)
        return len(self._L) == 0



class LazyListQueue(ListQueue):
    def __ini__(self):          # O(1)
        super().__init__()
        self._head = None       # index of first item in queue

    def enqueue(self, item):    # O(1)
        super().enqueue(item)
        if self._head is None: self._head = 0
    
    def dequeue(self):          # O(1) : lazy update gets us constant running time (on average)
        if self._head is None:
            raise IndexError("Can't dequeue from an empty queue!")
        
        item = self._L[self._head]
        self._head += 1
        
        if self._head > len(self._L)//2:   # When half of the list is garbage, trim the list
            self._L = self._L[self._head:] # Slice costs n/2, where n is length of list (including items to be deleted here)
            self._head = 0

        return item

    def __len__(self):          # O(1)
        return len(self._L) - self._head
