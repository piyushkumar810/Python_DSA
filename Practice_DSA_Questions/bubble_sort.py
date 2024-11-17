def bubble_sort(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                # see sewapping in python in very easy otherwise
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
                # otherwise
            '''temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp'''
    print(arr)

bubble_sort([3,5,1,2,4])

# the time complexity of this problem is = O(n^2)

# here the main disadvantage of this bubble sort is :
#   if you give sorted array then also it will take time complexity = O(n^2)