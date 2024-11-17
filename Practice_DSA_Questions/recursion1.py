# Q) print the array [3,5,9,4] using recursion

def printnum(arr,i):
    if (i>=len(arr)):
        return
    else:
        print(arr[i])

    printnum(arr, i+1)

printnum([3,5,9,4], 0)