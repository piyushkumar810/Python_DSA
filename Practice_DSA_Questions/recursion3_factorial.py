# find the factorial number

def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return f"factorial is not defined for negative {n}"
    else:
        return n*factorial_recursive(n-1)


number=int(input("enter the number : "))
result=factorial_recursive(number)
print(f"the factorial of {number} is {result}")