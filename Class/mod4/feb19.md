Linked List Implementation (head)

We need to define the list itself and the nodes.

Head of the list Create two methods, addfirst and removefirst both of which modify the beginning of the list. These will behave roughly like the push and operations of the stack.

```python
class LinkedList:
  def __init__(self):
    self._head = Implementation

  def addfirst(self, item):
    self._head = ListNode(item,self._head)

  def removefirst(self,item):
    item = self._head.data
    self._head = self._head.link
    return item


```
linked list implementation (tail)

Tail of the list: Create two methods, addlast, to be able to jump right to the end without traversing removelast a little by eliminating the link

```python
class LinkedList:
  def __init__(self):
    self._head = None
    self._tail = None

  def addfirst(self, item):
    self._head = ListNode(item, self._head)
    if self._tail is None: self._tail = self._head

  def addlast(self):
    if self._head is None:
      self.addfirst(item)

    else:
      self._tail.link = ListNode(item)
      self._tail = self._tail.link
  
  def removefirst(self):
    item = self._head.data
    self._head = self._head.link
    if self._head is None: self._tail = None
    return item
```


ListNode class

```python
class ListNode:
  def __init__(self, data, link=None, prev = None):
     self.data = data
    self.prev = prev
    self.link = link

    if prev is not None:
      prev.link = self

    if link is not None:
      link.prev = self

  def deletenode(node):
    node.data = node.link.data
    nide.link = node.link.link

  def i dont know():


   



  

```
