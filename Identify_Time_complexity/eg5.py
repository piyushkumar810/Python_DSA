def fun(n):
    i=1

    while(i<n):
        i=i*2
        print("hello")

fun(4)

# time complexity = O(log n)

# space complexity = O(1), because no extra space is taken in this problem

# q2)
def fun(n):
    for i in range(n):
        i=1

        while(i<n):
            i=i*2
            print("hello")

fun(4)

# time complexity = 
        #      for for loop = O(n)
        #            for while part = O(log n)
#            total= O(n) * O(log n)
#             T.C = O(n log n)

#             S.C = O(1), remains constant