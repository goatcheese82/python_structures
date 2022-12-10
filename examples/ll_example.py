class Directory():

   def __init__(self):
      self.head = None
      self.tail = None

   class Node:
      def __init__(self, data):
         self.data = data
         self.next = None
         self.previous = None

   def insert_head(self, value):
      new_node = Directory.Node(value)
      if self.head is None:
         self.head = new_node
         self.tail = new_node
      else:
         new_node.next = self.head
         self.head.previous = new_node
         self.head = new_node

   def insert_tail(self, value):
      new_node = Directory.Node(value)

      if self.head is None:
          self.head = new_node
          self.tail = new_node
      else:
          new_node.previous = self.tail
          self.tail.next = new_node
          self.tail = new_node

   def remove_head(self):
      if self.head == self.tail:
         self.head = None
         self.tail = None
      elif self.head is not None:
         self.head.next.previous = None
         self.head = self.head.next

   def remove_tail(self):
      self.tail.previous.next = None
      self.tail = self.tail.previous

   def remove(self, value):
       curr = self.head
       while curr is not None:
           if curr.data is value:
               if curr is self.head:
                   self.remove_head()
                   return
               elif curr is self.tail:
                   self.remove_tail()
                   return
               else:
                   curr.next.prev = curr.prev
                   curr.prev.next = curr.next
                   return
           curr = curr.next

   def replace(self, old_value, new_value):
       curr = self.head
       while curr is not None:
           if curr.data is old_value:
               curr.data = new_value
           curr = curr.next
   
   ############
   # Challenge#
   ############


   def _exists(self, value):
      """
      Create a helper that will check if the value exists in the directory.  If it does, it should return true. This will then be used to assure that duplicates are not inserted in the Directory.
      """

   def __iter__(self):
       current = self.head
       while current is not None:
           yield current.data
           current = current.next
   def __reversed__(self):
       current = self.tail
       while current is not None:
           yield current.data
           current = current.previous
   def __str__(self):
       output = "Directory["
       first = True
       for value in self:
           if first:
               first = False
           else:
               output += ", "
           output += str(value)
       output += "]"
       return output
   


d = Directory()
d.insert_tail("Harry")
d.insert_head("John")
d.insert_tail("John")
print(d)

#Return Directory["John", "Harry"]