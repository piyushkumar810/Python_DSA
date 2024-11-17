# Q) [3,5,9,4] print all the number in python using recursion but now in reverse order

def revnum(arr,i):
    if(i>=len(arr)):
        return
    else:
        print(arr[len(arr)-i-1])

    revnum(arr,i+1)

revnum([3,5,9,4], 0)
print("\n")

# --------------------------or (see power of recursion)

def printRev(arr,i):
    if(i>=len(arr)):
        return
    printRev(arr,i+1)
    print(arr[i])

printRev([3,5,9,4],0)