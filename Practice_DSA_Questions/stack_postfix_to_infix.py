# .----------------------------------------- postfix to infix conversion -------------------------------------------

stack=[]
operator=set(["+", "-", "*", "/", "^"])
expression="ab+c*"

for char in expression:
    if char not in operator:
        stack.append(char)
    else:
        op1=stack.pop()
        op2=stack.pop()
        stack.append(f"({op2} {char} {op1})")

print(stack.pop())