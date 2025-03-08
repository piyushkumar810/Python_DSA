def  func(n):
    for i in range(n):
        for j in range(n):
            print("hello")
            break

func(4)

# don't think for loop will always run n time only always check whole program 

# here , for i loop is running n times but for j is not running n times it will run only one time because 
#          inside it a break statement is used which will tirminate the program


# so, T.C = O(n) * O(1)
#             O(n * 1)= O(n)

# and, SC = o(1)