def fun(n):
    for i in range(n):
        for j in range(n):
            print("hello")

fun(1)
print("\n")

fun(2)
print("\n")

fun(3)
print("\n")

fun(4)

'''when n=1
   when i=0 --> j=0 , so 1 times hello printer'''

'''when n=2
   when i=0 --> j=0 - so hello printer , j=1 - so hello printer
   when i=1 --> j=0 - so hello printer , j=1 - so hello printer'''

# so finally
#  when n=1 } --> 1 time hello printed
#  when n=2 } --> 4 time hello printed 
#  when n=3 } --> 9 time hello printed 

# so,
#    time complexity = O(n^2)