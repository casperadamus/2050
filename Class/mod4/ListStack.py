# ListStack is an example of the wrapper pattern:
# We have 'wrapped' a python list into our own class, so we can control how the user accesses it
class ListStack:
   def __init__(self):    # O(1) 
      self._L = []        # Composition: A ListStack *has a* list

   def push(self, item):   # O(1)
      self._L.append(item)

   def pop(self):          # O(1)
      return self._L.pop()

   def peek(self):         # O(1)
      return self._L[-1]

   def __len__(self):      # O(1)
      return len(self._L)

   def isempty(self):          # O(1)
      return bool(len(self._L))

   # Unconvential repr defined below to help show stack during class
   def __repr__(self):
      width = 15
      return_string = ''
      for item in reversed(self._L):
         return_string += ' ' + '_'*(width-2) + ' ' + '\n'
         return_string += '|' + ' ' * (width-2) + '|' + '\n'
         return_string += '|' + str(item).center(width-2) + '|' + '\n'
         return_string += '|' + '_' * (width-2) + '|' + '\n'

      return return_string
    
if __name__ == '__main__':
   stk = ListStack()
   
   ##### Push #####
   stk.push(1)
   stk.push('hello')
   stk.push([1,2,3])

   print("top of stack: {}".format(stk.peek()))
   #### Quiz ####
   # 1) 1
   # 2) 'hello'
   # 3) [1,2,3]
   # 4) 3
   print(stk)


   print()
   print("stk.pop() = {}".format(stk.pop()))
   #### Quiz #### 
   # 1) 1
   # 2) 'hello'
   # 3) [1,2,3]
   # 4) 3
   print(stk)

