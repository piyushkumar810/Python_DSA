# -------------------------- Shunting Yard Algorithm -----------------------

def precedence(operator):
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "^":
        return 3
    return 0

def infixToPostfix(expression):
    stack = []  # Stack to hold operators
    output = []  # List to store the postfix expression

    for char in expression:
        if char.isalnum():  # If the character is an operand (A-Z, a-z, 0-9)
            output.append(char)
        elif char == "(":  # Left parenthesis -> Push to stack
            stack.append(char)
        elif char == ")":  # Right parenthesis -> Pop until '('
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()  # Remove '(' from stack
        else:  # Operator encountered
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    
    # Pop remaining operators in the stack
    while stack:
        output.append(stack.pop())

    return "".join(output)

# Example usage
infix = "(A+B)/C"
postfix = infixToPostfix(infix)
print(postfix)  # Expected Output: "AB+C/"
