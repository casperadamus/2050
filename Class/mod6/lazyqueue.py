class LazyQueue:
    def __init__(self):
        self._items = []
        self._head = 0  # Tracks the logical front of the queue

    def enqueue(self, x):
        """Adds an item to the end of the queue. O(1) amortized."""
        self._items.append(x)

    def dequeue(self):
        """Removes and returns the front item. O(1) amortized."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        item = self._items[self._head]
        self._head += 1
        
        # Cleanup step: if the 'dead' space at the front is more than half the list,
        # we compact it to prevent memory leaks.
        if self._head > len(self._items) // 2:
            self._compact()
            
        return item

    def _compact(self):
        """Removes the logically deleted elements from the physical list."""
        # Slice the list from the head to the end
        self._items = self._items[self._head:]
        # Reset the head pointer to the new start
        self._head = 0

    def is_empty(self):
        """Returns True if the queue is logically empty. O(1)."""
        return self.__len__() == 0

    def __len__(self):
        """Returns the number of logical items in the queue. O(1)."""
        return len(self._items) - self._head

    def __repr__(self):
        return f"LazyQueue({self._items[self._head:]})"
