# ------------------------------------insertion sort in python 

def insertion_sort(arr):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]

        # j is initialized to the index of the last element in the sorted portion of the array.
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        
        arr[j+1]=key
        
    return arr

arr=[10,2,5,14,-6]
sorted_list=insertion_sort(arr)
print(sorted_list)