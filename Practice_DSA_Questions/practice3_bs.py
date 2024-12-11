def bubble_sort_inhanced(arr):
    n=len(arr)

    for i in range(n-1):
        is_sorted=True
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                is_sorted=False
                arr[j],arr[j+1]=arr[j+1],arr[j]
            
        if(is_sorted==True):
            print("it is already sorted")
            break

    print(arr)

bubble_sort_inhanced([1,2,3,4,5])

