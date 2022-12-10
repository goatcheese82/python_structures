1. Introduction
   A basic structure in programming is the stack. A stack is a structure that is characterized by how the information is stored. We will discuss what a stack is and how to use it.
2. What is a stack?
   A stack is a data structure that is characterized by its last in/first out storage of items. We can think of a stack like a stack of pancakes, or cards, or really anything that is stacked. You place an item on top, and that is the next item that can be removed. So a stack is a structure that elements are added and removed from the end only.
3. How do we use stacks?
   A stack is used when we have a list of items of information that we want to store and access. In Python we add information to the stack with append(), and we remove information from the stack with pop().
      For example: 
      '''
      #our stack will be a list of types of vehicle

      stack = ['car', 'truck', 'van']

      # We can add vehicles to our stack with push()

      stack.append('bus')

      # stack now returns ['car', 'truck', 'van', 'bus']
      # notice that bus is at the end of the list

      # We can remove those items from the stack with pop()

      removed = stack.pop()

      # stack is now ['car', 'truck', 'van'] again and we have a new variable which is 'removed' which returns 'bus'

4. The function stack
   In Python, when we call a function, the interpreter will run it from top to bottom. This is how programs run, the interpreter will run the functions in a specific order.  This creates a call stack. As we traverse the call stack we might call additional functions, which might in turn call additional functions. As each function resolves, it is added to the stack.  This is why we call it the function stack. We can use this feature of programming to debug our programs, as if a function returns an error, it will be the last function in the stack.  By examining the stack we can see where we went wrong.

5. Analyzing stacks
   We can use the knowledge that a program will be executed as a stack, we can analyze the possible return values and behaviors of the program. As we review code, we want to know how the interpreter will prioritize the different parts. We can do this by creating diagrams that will give a visual representation of how the code is executed.  This can be done using a variety of different types of charts, but most commonly we can create a flow chart or a Unified Modeling Language Model, as well as a call tree.  The type of tool used to diagram a program depends on the complexity of the program, but all three can be very helpful.

6. Challenge:

   Create a list and remove the final item in that list and store it in a variable. Add another item to the list, then add the item stored in the variable.
