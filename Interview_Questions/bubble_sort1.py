# Q 1) when be will get maximum swap in bubble sort ?

# ans -> when array is in reversed order
# eg
# [1,2,3,4,5]--> this is already sorted so, you will not get maximum swap

# [3,2,4,1,5]--> here also you will not get maximum swap
 
# [5,4,3,2,1]--> but in this example you will get maximum swap, because this array is in reversied order

def bubble_sort(arr):
    n=len(arr)

    count=0
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):

                count+=1
                # see sewapping in python in very easy otherwise
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
                # otherwise
            '''temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp'''
    print(count)
    print(arr)

bubble_sort([3,5,1,2,4])