from ListStack import ListStack

# BadListStack is a ListStack (inheritance), but we override the push, pop, and peek methods.
# In BadListStack, we push to and pop from the beginning of the list instead of the end.
# This increases our running time to O(n) from O(1)

class BadListStack(ListStack):   # Inheritance: A BadListStack *is a* ListStack
   def push(self, item):         # O(n)
      self._L.insert(0, item)

   def pop(self):                # O(n)
      return self._L.pop(0)

   def peek(self):               # O(n)
      return self._L[0]

   # Unconvential repr defined below to help show stack during class
   def __repr__(self):
      width = 15
      return_string = ''
      for item in self._L:
         return_string += ' ' + '_'*(width-2) + ' ' + '\n'
         return_string += '|' + ' ' * (width-2) + '|' + '\n'
         return_string += '|' + str(item).center(width-2) + '|' + '\n'
         return_string += '|' + '_' * (width-2) + '|' + '\n'

      return return_string

if __name__ == '__main__':
   stk = BadListStack()
   
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