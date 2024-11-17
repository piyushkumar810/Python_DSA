# Q) can you solve the time complexity from O(n^2) --> O(n) when we give sorted array

def bubble_sort_enhanced(arr):
    n=len(arr)

    for i in range(n-1):
        is_sorted=True
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                is_sorted=False
                # see ewapping in python in very easy otherwise
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
                # otherwise
            '''temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp'''
        if(is_sorted==True):
            break
    print(arr)

# bubble_sort_enhanced([3,5,1,2,4])
bubble_sort_enhanced([1,2,3,4,5])