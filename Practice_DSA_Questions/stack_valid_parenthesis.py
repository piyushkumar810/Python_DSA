# -------------------------------- valid parenthesis --------------------------

stack = []  # Initialize an empty stack to store opening braces
open_braces = ["(", "{"]  # List of opening braces
closed_braces = [")", "}"]  # List of closing braces
string_input = "()"  # Input string containing braces

for i in string_input:
    if i in open_braces:
        stack.append(i)  # Push the opening brace onto the stack

    elif i not in open_braces and i in closed_braces and len(stack) != 0:
        index = closed_braces.index(i)  # Get the index of the closing brace
        if open_braces[index] == stack[len(stack)-1]:  
            stack.pop()  # If it matches the top of the stack, pop it

if len(stack) == 0:
    print("valid")  # If stack is empty, the brackets were properly matched
else:
    print("not valid")  # If stack is not empty, there are unmatched opening braces
