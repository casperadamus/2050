class Node:
    def __init__(self, item, link=None):
        self.item = item
        self.link = link
    
    def __repr__(self):
        return f"Node({self.item})"


class LinkedList:
    def __init__(self, items=None):
        self._len = 0
        self._head = None
        self._tail = None

        if items is not None:
            for item in items: 
                self.add_last(item)

    def __len__(self):
        return self._len

    def get_head(self):
        if self._head is None:
            return None
        return self._head.item

    def get_tail(self):
        if self._tail is None:
            return None
        return self._tail.item

    def add_first(self, item):
        new_node = Node(item)
        new_node.link = self._head
        self._head = new_node
        if len(self) == 0:
            self._tail = new_node
        self._len += 1

    def add_last(self, item):
        new_node = Node(item)
        if len(self) == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.link = new_node
            self._tail = new_node
        self._len += 1

    def remove_first(self):
        if len(self) == 0:
            raise RuntimeError("Cannot remove_first from an empty list.")

        removed_item = self._head.item
        self._head = self._head.link

        if self._head is None:
            self._tail = None

        self._len -= 1 
        return removed_item
    
    def remove_last(self):
        if len(self) == 0:
            raise RuntimeError("Cannot remove_last from an empty list.")

        removed_item = self._tail.item
        
        if len(self) == 1:
            self._head = None 
            self._tail = None
        else: 
            current = self._head
            while current.link is not self._tail:
                current = current.link

            current.link = None
            self._tail = current

        self._len -= 1 
        return removed_item
