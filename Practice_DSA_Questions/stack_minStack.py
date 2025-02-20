# ----------------------------------- minStack -----------------------------------

class MinStack:
    def __init__(self):
        self.stack = []      # Main stack to store all values
        self.minstack = []   # Stack to keep track of minimum values
        self.size = 0        # Size of the stack

    def push(self, val):
        """ Pushes val onto the stack and updates the min stack """
        if self.size == 0 or val <= self.minstack[-1]:  
            self.minstack.append(val)  # Store new minimum
        
        self.stack.append(val)  
        self.size += 1

    def pop(self):
        """ Removes the top element and updates the min stack """
        if self.stack:
            if self.stack[-1] == self.minstack[-1]:  
                self.minstack.pop()  # Only remove from minstack if it matches
            
            self.stack.pop()
            self.size -= 1

    def top(self):
        """ Returns the top element of the stack """
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """ Returns the minimum element in the stack """
        return self.minstack[-1] if self.minstack else None


# Testing the MinStack
minstack = MinStack()

# Pushing elements
minstack.push(5)
minstack.push(2)
minstack.push(8)
minstack.push(1)
minstack.push(3)

print("Top element:", minstack.top())  # Expected: 3
print("Minimum element:", minstack.getMin())  # Expected: 1

# Popping elements
minstack.pop()
print("Minimum after pop:", minstack.getMin())  # Expected: 1
minstack.pop()
print("Minimum after pop:", minstack.getMin())  # Expected: 2
