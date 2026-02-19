**Stack**
- A list with the restriction that insertion and deletion can only be performed only from one end, called the top
- push and poping elements  
- O(1)

**Stack Applications**
- example: is this is google docs, when you edit and you want to undo or redo option
- backtracking, computing the result 

```python
class ListStack:
  def __init__(self):
    self._L = []

  def push(self,item):
    self._L.append(item)

  def pop(self):
    return self._L.pop()

  def peek(self):
    return self._L[-1]

  def __len__(self):
    return len(self._L)
  
  def isempty(self):
    return len(self) == 0
    
```

**Queue**
- A list or collection with the restriction that insertion can be performed at one end and deletion can be performed at the other end
- First in First out 

```python 
class Queue:
  def __init__(self):
    self._head = 0
    self._L = []

  def enqueue(self,item):
    self._L.append(item)

  def dequeue(self):
    self._L.pop(0)

  def peek(self):
    return self.L[0]

  def __len__(self):
    return len(self._L)
 
  def isempty(self):
    return len(self) == 0


  
```
**Linked list** 
- doesn't store all data in a collection sequentially 
- Use a series of nodes, each of which stores:
    data
    the location of the next node

We want 2 classes:
  
```python
class Node:
  def __init__(self,v, link = None):
    self.value =  v
    self.link  = link 
    

class LinkedList:
```
