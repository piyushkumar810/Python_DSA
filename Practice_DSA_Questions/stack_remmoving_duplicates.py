# --------------------------------- removing dupliicates

def removeDuplicate(input_str):
    set_input = set()  # Use a set to track unique characters
    stack = []  # List to store unique characters in order

    for char in input_str:
        if char not in set_input:  # If char is seen for the first time
            stack.append(char)  # Add to stack (preserving order)
            set_input.add(char)  # Add to set to mark it as seen

    return "".join(stack)  # Join list into a string

input_string = "aabbcdcab"
result = removeDuplicate(input_string)
print(result)
