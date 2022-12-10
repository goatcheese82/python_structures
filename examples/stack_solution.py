class AddingMachine():
      def __init__(self):
         self.value = []
         self.last = []
      
      def _add(self, value):
         self.value.append(value)
         pass

      def _undo(self):
         self.last.append(self.value.pop())
         pass
      
      def _redo(self):
         self.value.append(self.last.pop())

      def _eval(self):
         value = sum(self.value)
         return value