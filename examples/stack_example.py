class AddingMachine():
      def __init__(self):
         self.value = []
      
      def _add(self, value):
         self.value.append(value)
         return

      def _undo(self):
         """
         Create a function to undo the last action.
         """
         pass
      
      def _redo(self):
         """
         Create a function to redo the last undo.
         """
         pass

      def _eval(self):
         value = sum(self.value)
         return value

am = AddingMachine()
am._add(3)
am._add(3)
am._add(2)
am._undo()
am._undo()
am._redo()

print(am._eval())

##Should return 6