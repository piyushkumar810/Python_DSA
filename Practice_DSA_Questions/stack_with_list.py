# --------------------------------- stack implementation with list -------------------------------------------

class Stack():
    def __init__(self):
        self.stack=[]

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def printResult(self):
        return self.stack
    
s=Stack()
s.push(5)
s.push(7)
s.push(10)
print(s.printResult())

s.pop()
print(s.printResult())