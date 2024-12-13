# print the number 1 to n using recursion 

def print_num(n):
    # base condition
    if n>0:
        # dividing the problems
        print_num(n-1)
        print(n)

print_num(6)
print("\n")

# printing opposit
def print_num(n):
    # base condition
    if n>0:
        # dividing the problems
        print(n)
        print_num(n-1)

print_num(6)
